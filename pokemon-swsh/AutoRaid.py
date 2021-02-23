import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class AutoRaid(JoycontrolPlugin):
    async def run(self):
        logger.info('Auto Raid Plugin loaded!')

        while True:
            await self.button_push('a')
            await self.wait(0.5)

            # Before a raid battle, press the "Don't Invite Others" button.
            # During a raid battle, press the "Pokemon" button.
            await self.button_push('up', press_time_sec=3.0)
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)

            # Cancel all when "Pokemon" is selected.
            for _ in range(3):
                await self.button_push('b')
                await self.wait(0.3)
            await self.button_push('up', press_time_sec=3.0)
            await self.wait(0.3)

            # Select the "Fight" Button or throw a wishing piece.
            for _ in range(3):
                await self.button_push('a')
                await self.wait(0.3)
                await self.button_push('down', press_time_sec=3.0)
                await self.button_push('up')
            
            # Cancel all when "Switch Pokemon" is selected.
            for _ in range(4):
                await self.button_push('b')
                await self.wait(0.3)

            # Select the "Next" button after the battle is finished.
            await self.button_push('down')
            await self.wait(0.1)
            await self.button_push('down')
            await self.wait(0.5)
