import logging
import datetime
import calendar
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class AutoLotoID(JoycontrolPlugin):
    def __init__(self, controller_state, options):
        super().__init__(controller_state, options)

        if options is None or len(options) < 4:
            raise JoycontrolPluginError('Plugin option not set. Please use "--plugin-options <lang_code> <year> <month> <day>".')

        self.lang_code = options[0]
        if self.lang_code not in ['ja']:
            raise JoycontrolPluginError(f'Invalid language code: {self.lang_code}')

        year = int(options[1])
        month = int(options[2])
        day = int(options[3])
        self.current_dt = datetime.datetime(year, month, day)


    async def set_datetime(self, current, next):
        diff = next - current
        if diff >= 0:
            for _ in range(diff):
                await self.button_push('up')
                await self.wait(0.1)
        else:
            for _ in range(diff * -1):
                await self.button_push('down')
                await self.wait(0.1)


    async def change_datetime_yyyymmdd(self, current_dt, next_dt):
        # year
        diff_year = next_dt.year - current_dt.year
        if diff_year >= 0:
            for _ in range(diff_year):
                await self.button_push('up')
                await self.wait(0.1)
        else:
            for _ in range(diff_year * -1):
                await self.button_push('down')
                await self.wait(0.1)

        await self.button_push('right')
        await self.wait(0.1)

        # month
        current_day = current_dt.day
        month = current_dt.month - 1
        while True:
            if month % 12 == next_dt.month - 1:
                break
            await self.button_push('up')
            await self.wait(0.1)

            month += 1

            if current_day > 28:
                max_day = calendar.monthrange(next_dt.year, month % 12 + 1)[1]
                if current_day > max_day:
                    current_day = max_day

        await self.button_push('right')
        await self.wait(0.1)

        # day
        max_day = calendar.monthrange(next_dt.year, next_dt.month)[1]
        day = current_day - 1
        while True:
            if day % max_day == next_dt.day - 1:
                break
            await self.button_push('up')
            await self.wait(0.1)
            day += 1

        await self.button_push('right')
        await self.wait(0.1)

        # hour
        hour = current_dt.hour
        while True:
            if hour % 24 == next_dt.hour:
                break
            await self.button_push('up')
            await self.wait(0.1)
            hour += 1

        await self.button_push('right')
        await self.wait(0.1)

        # minute
        minute = current_dt.minute
        while True:
            if minute % 24 == next_dt.minute:
                break
            await self.button_push('up')
            await self.wait(0.1)
            minute += 1

        await self.button_push('right')
        await self.wait(0.1)

        # ok
        await self.button_push('a')
        await self.wait(0.1)
        

    async def change_datetime(self, current_dt, next_dt, lang_code):
        if lang_code == 'ja':
            await self.change_datetime_yyyymmdd(current_dt, next_dt)
        else:
            # TODO: Other language
            await self.button_push('right', press_time_sec=1.0)
            await self.wait(0.1)
            await self.button_push('a')
            await self.wait(0.1)


    async def time_travel(self, current_dt, next_dt, lang_code):
        # Open the "Home"
        await self.button_push('home')
        await self.wait(0.5)

        # Open the "Home > System Settings"
        await self.button_push('down')
        await self.wait(0.2)
        await self.button_push('right', press_time_sec=1.0)
        await self.wait(0.2)
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
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.5)

        # Open the "Home > System Settings > System > Date and Time > Date and Time"
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('a')
        await self.wait(0.3)

        await self.change_datetime(current_dt, next_dt, lang_code)

        # Reopen the game.
        await self.button_push('home')
        await self.wait(1.0)
        await self.button_push('a')
        await self.wait(0.5)

    async def run(self):
        logger.info('Auto Loto-ID Plugin loaded!')

        for _ in range(15):
            await self.button_push('b')
            await self.wait(0.1)

        logger.info(self.current_dt)
        while True:
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('down')
            await self.wait(0.3)
            await self.button_push('a') # Select the try loto-ID
            await self.wait(0.8)

            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.3)
            await self.button_push('a')
            await self.wait(0.8)
            await self.button_push('a') # Save
            await self.wait(0.3)

            for _ in range(32):
                await self.button_push('b')
                await self.wait(0.3)

            next_dt = self.current_dt + datetime.timedelta(days=1)
            await self.time_travel(self.current_dt, next_dt, self.lang_code)
            self.current_dt = next_dt
            logger.info(self.current_dt)