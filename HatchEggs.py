import logging
import asyncio
from tqdm import tqdm
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class HatchEggs(JoycontrolPlugin):
    async def run(self):
        logger.info('Hatch Eggs Plugin loaded!')
        await self.reset_position()

        for egg_count in range(5):
            logger.info(f'egg_count: {egg_count + 1}')
            await self.hatch_eggs()
            await self.reset_position()
            await self.get_egg()

    async def reset_position(self):
        # Open menu
        await self.button_push('x')

        # Select TownMap
        await self.button_push('up', 'left', press_time_sec=1.0)
        await self.button_push('down')
        await self.button_push('a')
        await self.wait(3.0)

        # Select Route 5
        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(1.0)

        # Go to the pokemon nursery
        await self.left_stick('right')
        await self.wait(2.5)
        await self.left_stick('up')
        await self.wait(4.0)

        # Reset the left stick position
        await self.left_stick('center')
        await self.wait(0.01)
    
    async def hatch_eggs(self):
        await self.left_stick(angle=225)
        await self.wait(1.4)
        await self.left_stick('center')

        for lap in tqdm(range(60)):
            logger.debug(f'lap: {lap}')

            for angle in range(360):
                await self.left_stick(angle=angle)
                await self.wait(0.004)

                # Using the rotom turbo on the left side on lap 2/8.
                if lap % 8 == 1 and angle == 0:
                    logger.debug('turbo left')
                    asyncio.ensure_future(self.button_push('b'))
    
                # Using the rotom turbo on the right side on lap 6/8.
                elif lap % 8 == 5 and angle == 180:
                    logger.debug('turbo right')
                    asyncio.ensure_future(self.button_push('b'))

            asyncio.ensure_future(self.button_push('a'))
        
        # Reset the left stick position
        await self.left_stick('center')
        await self.wait(0.05)

        # Wait for the eggs to hatch.
        for _ in range(20):
            await self.button_push('a')
            await self.wait(0.3)

    async def get_egg(self):
        # Turn to the left
        await self.left_stick('left')
        await self.wait(0.1)
        await self.left_stick('center')
        await self.wait(0.1)

        # Talk to the breeder
        await self.button_push('a')
        await self.wait(0.8)
        await self.button_push('a')
        await self.wait(0.8)

        # Move to Yes or Cansel
        await self.button_push('down')
        await self.wait(0.1)
        await self.button_push('down')
        await self.wait(0.1)

        # Select Yes or Cancel
        await self.button_push('a')
        await self.wait(4.0)

        # End the talk
        await self.button_push('b')
        await self.wait(2.0)
        await self.button_push('b')
        await self.wait(2.0)
        await self.button_push('b')
        await self.wait(0.8)

        # Fine adjustment of position
        await self.left_stick('up')
        await self.wait(2.0)
        await self.left_stick('center')
        await self.wait(0.01)
