import logging
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class DistributeRaidFromBackup(JoycontrolPlugin):
    async def distribute_raid_from_backup(self):
    
        if self.options is None:
            raise JoycontrolPluginError('Plugin option is not set. Please use "--plugin-options <link_code>".')
        linkCode = self.options[0]

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
            if linkCode[0] == '0':
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('down')
                await self.wait(0.5)
            elif linkCode[0] == '1':
                await self.wait(0)
            elif linkCode[0] == '2':
                await self.button_push('right')
                await self.wait(0.5)
            elif linkCode[0] == '3':
                await self.button_push('right')
                await self.wait(0.5)
                await self.button_push('right')
                await self.wait(0.5)
            elif linkCode[0] == '4':
                await self.button_push('down')
                await self.wait(0.5)
            elif linkCode[0] == '5':
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('right')
                await self.wait(0.5)
            elif linkCode[0] == '6':
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('right')
                await self.wait(0.5)
                await self.button_push('right')
                await self.wait(0.5)
            elif linkCode[0] == '7':
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('down')
                await self.wait(0.5)   
            elif linkCode[0] == '8':
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('right')
                await self.wait(0.5)
            elif linkCode[0] == '9':
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('down')
                await self.wait(0.5)
                await self.button_push('right')
                await self.wait(0.5)
                await self.button_push('right')
                await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)     
            for num in range(1, 8):
                if linkCode[num - 1] == '0':
                    if linkCode[num] == '0':
                        await self.wait(0)
                    elif linkCode[num] == '1':
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                    elif linkCode[num] == '2':
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
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
                    elif linkCode[num] == '4':
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                    elif linkCode[num] == '5':
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                    elif linkCode[num] == '6':
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                    elif linkCode[num] == '7':
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                    elif linkCode[num] == '8':
                        await self.button_push('up')
                        await self.wait(0.5)
                    elif linkCode[num] == '9':
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                elif linkCode[num] == '0':
                    if linkCode[num - 1] == '1' or linkCode[num - 1] == '2' or linkCode[num - 1] == '3':
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                    elif linkCode[num - 1] == '4' or linkCode[num - 1] == '5' or linkCode[num - 1] == '6':
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                    elif linkCode[num - 1] == '7' or linkCode[num - 1] == '8' or linkCode[num - 1] == '9':
                        await self.button_push('down')
                        await self.wait(0.5)    
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 0:
                    await self.wait(0)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 1:
                    if int(linkCode[num - 1]) % 3 == 1 or int(linkCode[num - 1]) % 3 == 2:
                        await self.button_push('right')
                        await self.wait(0.5)
                    else:    
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 2:
                    if int(linkCode[num - 1]) % 3 == 1:
                        await self.button_push('right')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                    else:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 3:
                    await self.button_push('down')
                    await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 4:
                    if int(linkCode[num - 1]) % 3 == 1 or int(linkCode[num - 1]) % 3 == 2:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                    else:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 5:
                    if int(linkCode[num - 1]) % 3 == 0 or int(linkCode[num - 1]) % 3 == 2:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                    else:
                        await self.button_push('down')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 6:
                    await self.button_push('down')
                    await self.wait(0.5)
                    await self.button_push('down')
                    await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 7:
                    await self.button_push('down')
                    await self.wait(0.5)
                    await self.button_push('down')
                    await self.wait(0.5)
                    await self.button_push('right')
                    await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == 8:
                    await self.button_push('down')
                    await self.wait(0.5)
                    await self.button_push('down')
                    await self.wait(0.5)
                    await self.button_push('right')
                    await self.wait(0.5)
                    await self.button_push('right')
                    await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -1:
                    if int(linkCode[num - 1]) % 3 == 0 or int(linkCode[num - 1]) % 3 == 2:
                        await self.button_push('left')
                        await self.wait(0.5)
                    else:    
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -2:
                    if int(linkCode[num - 1]) % 3 == 0:
                        await self.button_push('left')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                    else:
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -3:
                    await self.button_push('up')
                    await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -4:
                    if int(linkCode[num - 1]) % 3 == 0 or int(linkCode[num - 1]) % 3 == 2:
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                    else:
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -5:
                    if int(linkCode[num - 1]) % 3 == 1 or int(linkCode[num - 1]) % 3 == 2:
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('right')
                        await self.wait(0.5)
                    else:
                        await self.button_push('up')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5)
                        await self.button_push('left')
                        await self.wait(0.5) 
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -6:
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -7:
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('left')
                    await self.wait(0.5)
                elif int(linkCode[num]) - int(linkCode[num - 1]) == -8:
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('up')
                    await self.wait(0.5)
                    await self.button_push('left')
                    await self.wait(0.5)
                    await self.button_push('left')
                    await self.wait(0.5)
                else:
                    raise ValueError('Invalid link code.')
                await self.button_push('a')
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
        logger.info('Distribute Raid From Backup Plugin loaded!')
        await self.distribute_raid_from_backup()
