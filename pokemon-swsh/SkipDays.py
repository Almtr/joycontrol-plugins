import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class SkipDays(JoycontrolPlugin):
    async def skip_days(self):

        daysLimitStr = input()
        daysLimit = int(daysLimitStr)
        daysNow = 0
        daysOfMonth = 0
        perCount = 0
        
        while daysNow < daysLimit:
         if daysOfMonth != 30:
           await self.button_push('a')
           await self.wait(0.25)
           await self.button_push('left')
           await self.wait(0.035)
           await self.button_push('left')
           await self.wait(0.035)
           await self.button_push('left')
           await self.wait(0.035)
           await self.button_push('up')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.2)
           daysNow += 1
           daysOfMonth += 1
        
         else:
           await self.button_push('a')
           await self.wait(0.25)
           await self.button_push('left')
           await self.wait(0.035)
           await self.button_push('left')
           await self.wait(0.035)
           await self.button_push('left')
           await self.wait(0.035)
           await self.button_push('up')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.035)
           await self.button_push('a')
           await self.wait(0.2)
           daysOfMonth = 0
        
         if int(daysNow / daysLimit * 100) > perCount:
           logger.info(str(int(daysNow / daysLimit * 100)) + '% (' + str(daysNow) + 'days) finished')
           perCount = int(daysNow / daysLimit * 100)
           
        await self.button_push('home')
        await self.wait(1)
        await self.button_push('a')


    async def run(self):
        logger.info('Skip Days Plugin loaded!')
        print('\nEnter the number of days you want')
        await self.skip_days()
