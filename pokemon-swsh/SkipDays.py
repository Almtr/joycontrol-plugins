import logging
from aioconsole import ainput
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class SkipDays(JoycontrolPlugin):
    async def skip_days(self, daysLimit):
        daysNow = 0
        daysOfMonth = 0
        perCount = 0

        # Reset cursor position
        await self.button_push('a')
        await self.wait(0.5)
        await self.button_push('right', press_time_sec = 0.55)
        await self.wait(0.055)
        await self.button_push('a')
        await self.wait(1)

        while daysNow < daysLimit:
            if daysOfMonth != 30:
                daysNow += 1
                daysOfMonth += 1
            else:
                daysOfMonth = 0

            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('left')
            await self.wait(0.055)
            await self.button_push('left')
            await self.wait(0.055)
            await self.button_push('left')
            await self.wait(0.055)
            await self.button_push('up')
            await self.wait(0.055)
            await self.button_push('right', press_time_sec = 0.55)
            await self.wait(0.055)
            await self.button_push('a')
            await self.wait(0.3)

            if int(daysNow / daysLimit * 100) > perCount:
                logger.info(str(int(daysNow / daysLimit * 100)) + '% (' + str(daysNow) + 'days) finished')
                perCount = int(daysNow / daysLimit * 100)

        await self.button_push('home')
        await self.wait(1)
        await self.button_push('a')


    async def run(self):
        logger.info('Skip Days Plugin loaded!')

        if self.options is None:
            raise JoycontrolPluginError('Plugin option is not set. Please use "--plugin-options <days>".')

        daysLimit = int(self.options[0])

        if daysLimit >= 10000:
            while True:
                answer = await ainput(prompt='The action you want may fail. Do you want to continue?(y/n)')

                if 'n' in answer.lower():
                    return
                elif 'y' in answer.lower():
                    break
                else:
                    print('Invalid input. Please answer \'y\' or \'n\'')

        await self.skip_days(daysLimit)
