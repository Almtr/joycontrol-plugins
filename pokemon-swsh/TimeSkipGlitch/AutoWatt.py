import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from TimeSkipBasePlugin import TimeSkipBasePlugin

logger = logging.getLogger(__name__)

class AutoWatt(TimeSkipBasePlugin):
    async def run(self):
        logger.info('Auto Watt Plugin loaded!')

        '''
        Reference:
          https://github.com/watagi/AutoWatt
        '''

        while True:
            await self.button_push('a') # Select a den
            await self.wait(0.3)

            # Close the all messages
            for _ in range(10):
                await self.button_push('b')
                await self.wait(0.3)

            await self.change_year()
            await self.wait(1.0)