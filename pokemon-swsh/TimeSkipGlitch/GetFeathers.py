import logging
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
from TimeSkipBasePlugin import TimeSkipBasePlugin

logger = logging.getLogger(__name__)

class GetFeathers(TimeSkipBasePlugin):
    async def use_flying_taxi(self):
        # Open menu
        await self.button_push('x')

        # Select TownMap
        await self.button_push('up', 'left', press_time_sec=1.0)
        await self.button_push('down')
        await self.button_push('a')
        await self.wait(3.0)

        # Select current position
        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(3.0)


    async def run(self):
        logger.info('Get Feathers Plugin loaded!')

        lap = 1
        while True:
            logger.info(f'{lap} lap')
            lap += 1

            # Reset position
            await self.use_flying_taxi()

            # 1st feather
            await self.left_stick('right')
            await self.wait(1.7)
            await self.left_stick('up')
            await self.wait(2.7)
            await self.left_stick('right')
            await self.wait(3.1)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            # 2nd feather
            await self.left_stick(angle=158)
            await self.wait(1.9)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            # 3rd feather
            await self.left_stick(angle=192)
            await self.wait(1.5)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            # 4th feather
            await self.left_stick(angle=197)
            await self.wait(1.3)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            # 5th feather
            await self.left_stick(angle=145)
            await self.wait(0.75)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            # 6th feather
            await self.left_stick(angle=190)
            await self.wait(2.58)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            # 7th feather
            await self.left_stick(angle=150)
            await self.wait(1.7)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            # 8th feather
            await self.left_stick(angle=215)
            await self.wait(2.0)
            await self.left_stick('center')
            await self.wait(0.8)
            await self.button_push('a')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(0.5)

            await self.change_year()
            await self.wait(1.0)