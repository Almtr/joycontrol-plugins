import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class AutoRaid(JoycontrolPlugin):
    async def run(self):
        logger.info('Auto Raid Plugin loaded!')

        while True:
            await self.button_push('a') # Select the "Fight" button
            await self.wait(0.1)
            await self.button_push('up')
            await self.wait(0.3)
            await self.button_push('a') # Select the "Next" button
            await self.wait(0.1)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.1)
            await self.button_push('up', press_time_sec=3.0)
            await self.wait(0.3)