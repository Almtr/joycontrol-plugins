import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class ReleasePokemons(JoycontrolPlugin):
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


    async def run(self):
        logger.info('Release Pokemons Plugin loaded!')

        logger.info('Reset corsor position.')
        for _ in range(15):
            await self.button_push('b')
            await self.wait(0.3)
        await self.open_pokemon_box()

        logger.info('Start releasing pokemons in a box')
        for _ in range(5): # row
            for _ in range(6): # column
                await self.release_pokemon()
                await self.button_push('right')
                await self.wait(0.3)

            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('right')
            await self.wait(0.3)
        logger.info('Finish releasing pokemons in a box')