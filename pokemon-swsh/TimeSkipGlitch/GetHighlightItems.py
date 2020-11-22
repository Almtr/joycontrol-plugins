import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from TimeSkipBasePlugin import TimeSkipBasePlugin

logger = logging.getLogger(__name__)

class GetHighlightItems(TimeSkipBasePlugin):
    async def run(self):
        logger.info('Get Highlight Items Plugin loaded!')

        lap = 1
        while True:
            logger.info(f'{lap} lap')
            lap += 1

            # Talk to the shop clerk
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.8)

            # Select Highlight Items
            await self.button_push('down')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.8)

            # Buy items
            await self.button_push('a')
            await self.wait(0.8)

            # Close all messages
            for _ in range(20):
                await self.button_push('b')
                await self.wait(0.3)

            await self.change_year()
            await self.wait(1.0)