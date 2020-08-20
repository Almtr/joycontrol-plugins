import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from TimeSkipBasePlugin import TimeSkipBasePlugin

logger = logging.getLogger(__name__)

class ChangeRaidPokemon(TimeSkipBasePlugin):
    async def run(self):
        logger.info('Change Raid Pokemon Plugin loaded!')

        lap = 0
        while True:
            for i in range(3):
                # Examine a den
                await self.button_push('a')
                await self.wait(0.6)

                # Get watt
                if i > 0:
                    await self.button_push('a')
                    await self.wait(0.3)
                    await self.button_push('a')
                    await self.wait(0.3)
                    await self.button_push('a')
                    await self.wait(0.6)

                await self.button_push('a')
                await self.wait(1.8)
                await self.change_days(1)
                await self.wait(0.3)

                # Exit
                await self.button_push('b')
                await self.wait(0.8)
                await self.button_push('a')
                await self.wait(3.8)

            # Show a 4th Pokemon
            await self.button_push('a')
            await self.wait(0.6)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)    
            await self.button_push('a')
            await self.wait(0.6)    
            
            # Instead of alarm
            for _ in range(10):
                await self.button_push('down')
                await self.wait(0.1)
                await self.button_push('up')
                await self.wait(0.1)

            # Reset game and days
            await self.wait(2)
            await self.button_push('home')
            await self.wait(1)
            await self.button_push('x')
            await self.wait(1.5)
            await self.button_push('a')
            await self.wait(4)
            await self.change_days(-3)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(20)
            await self.button_push('a')
            await self.wait(10)        

            lap += 1
            logger.info(str(lap) + 'cycle finished.')