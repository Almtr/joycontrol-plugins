import logging
import asyncio

from tqdm import tqdm
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class HatchEggs(JoycontrolPlugin):
    async def run(self):
        logger.info('Hatch Eggs Plugin loaded!')

        egg_count = 0
        for _ in range(6): # 1 box (5 x 6 = 30)
            for _ in range(5):
                logger.info(f'egg_count: {egg_count + 1}')

                await self.reset_position()
                await self.get_egg()
                await self.hatch_eggs()
                egg_count += 1

            await self.open_pokemon_box()
            await self.put_pokemon_in_box(egg_count)

    async def reset_position(self):
        # Open menu
        await self.button_push('x')

        # Select TownMap
        await self.button_push('up', 'left', press_time_sec=1.0)
        await self.button_push('down')
        await self.button_push('a')
        await self.wait(3.0)

        # Select Route 5
        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(1.0)

        # Go to the pokemon nursery
        await self.left_stick('right')
        await self.wait(2.5)
        await self.left_stick('up')
        await self.wait(4.0)

        # Reset the left stick position
        await self.left_stick('center')
        await self.wait(0.01)
    
    async def hatch_eggs(self):
        await self.left_stick(angle=200)
        await self.wait(2.0)
        await self.left_stick('center')

        for lap in tqdm(range(80)):
            logger.debug(f'lap: {lap}')

            # Rotate
            for angle in range(360):
                await self.left_stick(angle=angle)
                await self.wait(0.003)

                # Using the rotom turbo on the left side on lap 2/10.
                if lap % 10 == 1 and angle == 0:
                    logger.debug('turbo left')
                    asyncio.ensure_future(self.button_push('b'))
    
                # Using the rotom turbo on the right side on lap 7/10.
                elif lap % 10 == 6 and angle == 180:
                    logger.debug('turbo right')
                    asyncio.ensure_future(self.button_push('b'))

            asyncio.ensure_future(self.button_push('a'))
        
        # Reset the left stick position
        await self.left_stick('center')
        await self.wait(0.05)

        # Wait for the eggs to hatch.
        for _ in range(20):
            await self.button_push('b')
            await self.wait(0.3)

    async def get_egg(self):
        # Turn to the left
        await self.left_stick('left')
        await self.wait(0.1)
        await self.left_stick('center')
        await self.wait(0.1)

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

        await self.left_stick('center')
        await self.wait(0.01)

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