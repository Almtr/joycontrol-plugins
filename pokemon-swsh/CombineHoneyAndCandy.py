import logging
import datetime
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class CombineHoneyAndCandy(JoycontrolPlugin):
    def __init__(self, controller_state, options):
        super().__init__(controller_state, options)

        if options is None or len(options) < 2:
            raise JoycontrolPluginError('Plugin option not set. Please use "--plugin-options <honey_num> <rare_candy_num>".')

        self.honey_num = int(options[0])
        self.rare_candy_num = int(options[1])


    async def combine_items_3honey_1candy(self):
        await self.button_push('a')
        await self.wait(0.3)
        await self.button_push('a') # Combine items
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(2.0)
        await self.button_push('a')
        await self.wait(3.0)

        await self.button_push('right') # Go to the "Honey"
        await self.wait(0.5)

        # Select three berries
        await self.button_push('a')
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(0.3)
        await self.button_push('a')
        await self.wait(0.3)

        await self.button_push('left') # Go to the "Rare Candy"
        await self.wait(0.5)

        # Select a candy
        await self.button_push('a')
        await self.wait(0.8)

        await self.button_push('a') # Yes
        await self.wait(1.5)

        # Close messages
        await self.button_push('a')
        await self.wait(1.5)

        await self.button_push('a')
        await self.wait(5.0)

        await self.button_push('a')
        await self.wait(5.0)

        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(0.8)
    

    def __calc_total_count(self, honey, rare_candy):
        max_honey = int(honey / 3)
        max_candy = rare_candy

        if max_honey < max_candy:
            return max_honey
        return max_candy
    

    async def combine_items(self, total):
        for count in range(total):
            await self.combine_items_3honey_1candy()
            logger.info(f'{count + 1}/{total} items were combined.')


    async def run(self):
        logger.info('Combine three honeys and one candy Plugin loaded!')

        total = self.__calc_total_count(self.honey_num, self.rare_candy_num)

        now = datetime.datetime.now()
        end_datetime = now + datetime.timedelta(seconds=total * 25)
        logger.info(f'Estimated end time: {end_datetime}.')

        await self.combine_items(total)