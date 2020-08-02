import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class ReleasePokemons(JoycontrolPlugin):
    async def change_release_mode(self):
        # Select a pokemon
        await self.button_push('a')
        await self.wait(0.3)

        # Move until the "Release"
        await self.button_push('up')
        await self.wait(0.3)
        await self.button_push('up')
        await self.wait(0.3)

        # Select the "Release"
        await self.button_push('a')
        await self.wait(0.8)

        # Select more Pokemon
        await self.button_push('down')
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(1.5)


    async def select_next_pokemon(self, release_num):
        num = release_num % 60

        if num % 60 == 29 or num % 60 == 59:
            return

        # Go to the next line
        if num % 12 == 5 or num % 12 == 11:
            if num < 30:
                await self.button_push('down')
            else:
                await self.button_push('up')

        # Odd rows move to the right
        elif num % 12 < 5:
            await self.button_push('right')

        # Even rows move to the left
        elif num % 12 < 11:
            await self.button_push('left')
        
        await self.wait(0.5)


    async def release_all(self):
        # Select the "Release All"
        await self.button_push('plus')
        await self.wait(0.8)

        # Select the "Release"
        await self.button_push('up')
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(0.8)

        # Close a message
        await self.button_push('a')
        await self.wait(0.8)


    async def run(self):
        logger.info('Release Pokemons Plugin loaded!')

        box = 3
        release_num = 0

        for _ in range(box):
            await self.change_release_mode()

            await self.button_push('a')
            await self.wait(0.1)

            for i in range(30):
                for _ in range(3):
                    await self.button_push('a')
                    await self.wait(0.1)
                await self.select_next_pokemon(release_num)
                release_num += 1

            await self.release_all()

            # Go to the next box
            await self.button_push('r')
            await self.wait(0.3)

        await self.button_push('plus')
        await self.wait(0.8)