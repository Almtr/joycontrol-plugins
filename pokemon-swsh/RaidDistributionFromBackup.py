import logging
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class RaidDistributionFromBackup(JoycontrolPlugin):
    async def raid_distribution_from_backup(self):

        linkCode = self.options[0]
        if self.options is None:
            raise JoycontrolPluginError('Plugin option is not set. Please use "--plugin-options <link_code>".')

        num = 0
        count = 0

        while True:
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(20)
            await self.button_push('up' , 'x', 'b')
            await self.wait(3)
            await self.button_push('a')
            await self.wait(2)
            await self.button_push('a')
            await self.wait(10)
            await self.button_push('y')
            await self.wait(1)
            await self.button_push('plus')
            await self.wait(20)
            await self.button_push('b')
            await self.wait(0.5)
            await self.button_push('b')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(4)
            await self.button_push('plus')
            await self.wait(1)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            for num in range(8):
                if linkCode[num] == '0':
                    await self.button_push('a')
                    await self.wait(0.5)
                elif linkCode[num] == '1':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('left')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                elif linkCode[num] == '2':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                elif linkCode[num] == '3':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('right')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)         
                elif linkCode[num] == '4':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('left')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                elif linkCode[num] == '5':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                elif linkCode[num] == '6':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('right')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                elif linkCode[num] == '7':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('left')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                elif linkCode[num] == '8':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
                elif linkCode[num] == '9':
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('right')
                    await self.wait(0.5)
                    await self.button_push('a')
                    await self.wait(0.5)
                    if num != 7:
                        await self.button_push('down')
                        await self.wait(0.5)
           
            await self.button_push('plus')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(60)
            await self.button_push('up')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.7)
            await self.button_push('a')
            await self.wait(0.7)
            await self.button_push('a')
            await self.wait(0.7)
            await self.button_push('a')
            await self.wait(15)
            await self.button_push('home')
            await self.wait(1.5)
            await self.button_push('x')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(5)
            count += 1
            logger.info(str(count) + 'cycle finished.')        
       
       
    async def run(self):
        logger.info('Raid Distribution From Backup Plugin loaded!')
        await self.raid_distribution_from_backup()
