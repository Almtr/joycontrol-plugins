import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from TimeSkipBasePlugin import TimeSkipBasePlugin

logger = logging.getLogger(__name__)

class BuyBargains(TimeSkipBasePlugin):
    async def run(self):
        logger.info('Buy Bargains Plugin loaded!')

        lap = 1
        while True:
            logger.info(f'buy {lap} items')
            lap += 1

            # Talk to clerk
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.8)

            # Close the all messages
            for _ in range(18):
                await self.button_push('b')
                await self.wait(0.3)

            await self.change_year()
            await self.wait(1.0)