import logging
import datetime
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class ReleasePokemons(JoycontrolPlugin):
    def __init__(self, controller_state, options):
        super().__init__(controller_state, options)

        self.box = 1
        if options is not None:
            self.box = int(options[0])

        if not 1 <= self.box <= 32:
            raise JoycontrolPluginError('Number of boxes must be in 1-32.')


    async def release_pokemon(self):
        # Select a pokemon
        await self.button_push('a')
        await self.wait(0.3)

        # Move until "release"
        await self.button_push('up')
        await self.wait(0.3)
        await self.button_push('up')
        await self.wait(0.3)

        # Select "release"
        await self.button_push('a')
        await self.wait(0.8)

        # Select "yes"
        await self.button_push('up')
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(1.5)

        # Remove a message
        await self.button_push('a')
        await self.wait(0.3)


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


    async def select_next_pokemon(self, release_num):
        num = release_num % 60

        # Go to the next box
        if num == 29 or num == 59:
            await self.button_push('r')

        # Go to the next line
        elif num % 12 == 5 or num % 12 == 11:
            if num < 30:
                await self.button_push('down') # Odd boxes
            else:
                await self.button_push('up') # Even boxes

        # Odd rows move to the right
        elif num % 12 < 5:
            await self.button_push('right')

        # Even rows move to the left
        elif num % 12 < 11:
            await self.button_push('left')
        
        await self.wait(0.5)

    async def release_pokemons(self, total):
        for num in range(total):
            await self.release_pokemon()
            logger.info(f'{num + 1}/{total} pokemons released.')
            await self.select_next_pokemon(num)


    async def run(self):
        logger.info('Release Pokemons Plugin loaded!')
        
        release_num = self.box * 30

        now = datetime.datetime.now()
        end_datetime = now + datetime.timedelta(seconds=release_num * 5 + 16)
        logger.info(f'Estimated end time: {end_datetime}.')

        logger.info('Reset corsor position.')
        for _ in range(12): # Cancel all
            await self.button_push('b')
            await self.wait(0.3)
        await self.open_pokemon_box()

        logger.info('Start releasing pokemons.')
        await self.release_pokemons(release_num)
        logger.info('Finish releasing pokemons.')