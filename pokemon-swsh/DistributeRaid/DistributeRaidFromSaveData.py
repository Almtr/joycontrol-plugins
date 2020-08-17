import logging
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError
import os
import sys

sys.path.append(os.path.abspath(os.path.dirname(__file__)))
import Keypad

logger = logging.getLogger(__name__)

class DistributeRaidFromSaveData(JoycontrolPlugin):
    async def push_linkcode(self, linkcode):
        keypad = Keypad.Keypad()
        current_num = 1 # init position
        for num in linkcode:
            target_num = int(num)
            path = keypad.shortest_path(current_num, target_num)
            for button in path:
                await self.button_push(button) # Move to target number
                await self.wait(0.5)
            await self.button_push('a') # Push number
            await self.wait(0.5)
            current_num = target_num

    async def distribute_raid_from_save_data(self):

        if self.options is None:
            raise JoycontrolPluginError('Plugin option is not set. Please use "--plugin-options <link_code>".')
        linkCode = self.options[0]
        if not linkCode.isdecimal() or len(linkCode) != 8:
            raise ValueError('Invalid link code.')

        count = 0

        while True:
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(20)
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
            await self.push_linkcode(linkCode)                               
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
        logger.info('Distribute Raid From Save Data Plugin loaded!')
        await self.distribute_raid_from_save_data()
