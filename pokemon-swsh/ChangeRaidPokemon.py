import logging
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class ChangeRaidPokemon(JoycontrolPlugin):
    async def run(self):
        logger.info('Change Raid Pokemon Plugin loaded!')

        lap = 0
        while True:
            first = True
            for _ in range(3):
                if first:
                    await self.button_push('a')
                    await self.wait(0.6)
                    await self.button_push('a')
                    await self.wait(1.8)
                    first = False
                else:
                    await self.button_push('a')
                    await self.wait(0.6)
                    await self.button_push('a')
                    await self.wait(0.3)
                    await self.button_push('a')
                    await self.wait(0.3)
                    await self.button_push('a')
                    await self.wait(0.6)
                    await self.button_push('a')
                    await self.wait(1.8)
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

                # Set to next day
                await self.button_push('a')
                await self.wait(0.1)
                await self.button_push('a')
                await self.wait(0.1)
                await self.button_push('up')
                await self.wait(0.1)
                await self.button_push('right', press_time_sec=0.5)
                await self.wait(0.1)
                await self.button_push('a')
                await self.wait(0.1)

                # Reopen the game.
                await self.button_push('home')
                await self.wait(1.0)
                await self.button_push('a')
                await self.wait(0.8)
                await self.button_push('b')
                await self.wait(0.8)
                await self.button_push('a')
                await self.wait(3.8)
                
            await self.button_push('a')
            await self.wait(0.6)
            await self.button_push('a')
            await self.wait(0.4)
            await self.button_push('a')
            await self.wait(0.4)    
            for _ in range(10):
                await self.button_push('down')
                await self.wait(0.1)
                await self.button_push('up')
                await self.wait(0.1)
            await self.wait(2)
            await self.button_push('home')
            await self.wait(1)
            await self.button_push('x')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(4)
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

            # Down three days
            await self.button_push('a')
            await self.wait(0.1)
            await self.button_push('a')
            await self.wait(0.1)
            await self.button_push('down')
            await self.wait(0.1)
            await self.button_push('down')
            await self.wait(0.1)
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
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(20)
            await self.button_push('a')
            await self.wait(10)        
            lap += 1
            logger.info(str(lap) + 'cycle finished.')
