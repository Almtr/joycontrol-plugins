import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class TimeSkipBasePlugin(JoycontrolPlugin):

    async def open_date_and_time_settings(self):
        # Open the "Home"
        await self.button_push('home')
        await self.wait(0.8)

        # Open the "Home > System Settings"
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('right', press_time_sec=0.8)
        await self.wait(0.1)
        await self.button_push('left')
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.8)

        # Open the "Home > System Settings > System"
        await self.button_push('down', press_time_sec=1.5)
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(0.3)

        # Open the "Home > System Settings > System > Date and Time"
        await self.button_push('down', press_time_sec=0.6)
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.5)

        # Open the "Home > System Settings > System > Date and Time > Date and Time"
        await self.button_push('down', press_time_sec=0.7)
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.3)

    async def change_year(self):
        await self.open_date_and_time_settings()

        # Set next year
        await self.button_push('up')
        await self.wait(0.1)
        await self.button_push('right', press_time_sec=1.0)
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.1)

        await self.button_push('a')
        await self.wait(0.1)

        # Set previous year
        await self.button_push('left', press_time_sec=1.0)
        await self.wait(0.1)
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('right', press_time_sec=1.0)
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.1)

        # Reopen the game.
        await self.button_push('home')
        await self.wait(1.0)
        await self.button_push('a')
        await self.wait(0.5)


    async def change_days(self, days):
        await self.open_date_and_time_settings()

        # Update days
        await self.button_push('a')
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.1)

        if days >= 0:
            for _ in range(days):
                await self.button_push('up')
                await self.wait(0.1)
        else:
            for _ in range(days * -1):
                await self.button_push('down')
                await self.wait(0.1)

        await self.button_push('right', press_time_sec=0.5)
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.1)

        # Reopen the game.
        await self.button_push('home')
        await self.wait(1.0)
        await self.button_push('a')
        await self.wait(0.5)