import logging
import time
import datetime
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class HatchEggs(JoycontrolPlugin):
    def __init__(self, controller_state, options):
        super().__init__(controller_state, options)

        if options is None or len(options) < 2:
            raise JoycontrolPluginError('Plugin option not set. Please use "--plugin-options <egg cycle> <total of eggs>".')

        self.egg_cycle = int(options[0])
        self.total_eggs = int(options[1])

        if not 5 <= self.egg_cycle <= 40:
            raise JoycontrolPluginError('Egg cycle must be in 5-40.')
        
        if not 1 <= self.total_eggs <= 960:
            raise JoycontrolPluginError('Total of eggs must be in 1-960.')


    def __calc_hatching_time(self, egg_cycle):
        return egg_cycle * 2.75 + 25

    
    def __calc_end_datetime(self, egg_cycle, total_eggs):
        now = datetime.datetime.now()
        hatching_time = self.__calc_hatching_time(egg_cycle)
        get_egg_time = 25
        put_pokemon_time = 14
        estimated_time = (hatching_time + get_egg_time) * total_eggs + put_pokemon_time * int(total_eggs / 5)
        return now + datetime.timedelta(seconds=estimated_time)


    async def open_pokemon_box(self):
        # Open menu
        await self.button_push('x')

        # Select pokemon menu
        await self.button_push('up', 'left', press_time_sec=1.0)
        await self.button_push('a')
        await self.wait(2.0)

        # Enter pokemon box
        await self.button_push('r')
        await self.wait(2.0)


    async def put_pokemon_in_box(self, egg_count):
        await self.open_pokemon_box()

        # Switch range mode
        await self.button_push('y')
        await self.wait(0.3)

        await self.button_push('y')
        await self.wait(0.3)

        # # Move to party area
        await self.button_push('left')
        await self.wait(0.3)

        # Move to second pokemon position
        await self.button_push('down')
        await self.wait(0.3)

        # Grub pokemons
        await self.button_push('a')
        await self.wait(0.3)
        await self.button_push('down', press_time_sec=1.0)
        await self.button_push('a')
        await self.wait(0.3)

        # Move to pokemon list
        await self.button_push('down', press_time_sec=1.0)
        await self.button_push('right')
        await self.wait(0.3)

        # Select box list and put pokemons in current box
        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(0.3)
        await self.button_push('b')
        await self.wait(0.3)

        # Move to next box
        if egg_count % 30 == 0:
            await self.button_push('r')
            await self.wait(0.3)

        # Cancel All
        for _ in range(12):
            await self.button_push('b')
            await self.wait(0.3)


    async def hatch_egg(self, hatching_time):
        start_time = time.time()
        elapsed_time = 0

        await self.left_stick(angle=145)
        await self.wait(1.0)

        await self.left_stick('left')
        await self.right_stick('right')

        # Wait until the rotom turbo becomes available.
        await self.wait(5.0)

        while elapsed_time < hatching_time:
            await self.button_push('b')
            elapsed_time = time.time() - start_time

        await self.left_stick('center')
        await self.right_stick('center')


    async def get_egg(self):
        # Move to the front of the breeder
        await self.left_stick('down', power=1100)
        await self.wait(1.8)
        await self.left_stick('right')
        await self.wait(0.3)
        await self.left_stick('center')

        # Talk to the breeder
        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(0.8)

        # Move to Yes or Cansel
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('down')
        await self.wait(0.1)

        # Select Yes or Cancel
        await self.button_push('a')
        await self.wait(4.0)

        # End the talk
        await self.button_push('b')
        await self.wait(2.0)
        await self.button_push('b')
        await self.wait(2.0)
        await self.button_push('b')
        await self.wait(0.8)


    async def use_flying_taxi(self):
        # Open menu
        await self.button_push('x')

        # Select TownMap
        await self.button_push('up', 'left', press_time_sec=1.0)
        await self.button_push('down')
        await self.button_push('a')
        await self.wait(3.0)

        # Select current position
        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(3.0)


    async def hatch_eggs(self, total_eggs, hatching_time):
        egg_count = 0
        for _ in range(total_eggs):
            await self.use_flying_taxi() # Reset position
            await self.get_egg()
            egg_count += 1

            logger.info(f'{egg_count}/{total_eggs} egg: Start hatching the egg.')
            await self.hatch_egg(hatching_time)
            logger.info(f'{egg_count}/{total_eggs} egg: Finish hatching the egg.')

            # When you get 5 Pokemon, put them in the pokemon box.
            if egg_count % 5 == 0:
                await self.put_pokemon_in_box(egg_count)


    async def run(self):
        logger.info('Hatch Eggs Plugin loaded!')
        hatching_time = self.__calc_hatching_time(self.egg_cycle)
        end_datetime = self.__calc_end_datetime(self.egg_cycle, self.total_eggs)

        logger.info(f'Estimated end time: {end_datetime}.')
        await self.hatch_eggs(self.total_eggs, hatching_time)