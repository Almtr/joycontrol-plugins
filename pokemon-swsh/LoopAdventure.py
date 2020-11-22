import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class LoopAdventure(JoycontrolPlugin):
    async def loop_adventure(self):
        '''
        Commands:
          AAAAA (wait 5sec) DOWN A (wait 3sec) 
          B (wait 2sec) B DOWN A (wait 3sec) DOWN
        References:
          - https://twitter.com/dura_calen/status/1322059379613474816
          - https://twitter.com/dura_calen/status/1322878410872430592
        '''

        while True:
            for _ in range(5):
                await self.button_push('a')
                await self.wait(1.0)
            await self.wait(4.0)            
            await self.button_push('down')
            await self.wait(1.0)
            await self.button_push('a')
            await self.wait(3.0)            
            await self.button_push('b')
            await self.wait(2.0)
            await self.button_push('b')
            await self.wait(1.0)
            await self.button_push('down')
            await self.wait(1.0)
            await self.button_push('a')
            await self.wait(3.0)            
            await self.button_push('down')
            await self.wait(1.0)

    async def run(self):
        logger.info('Loop Adventure Plugin loaded!')
        await self.loop_adventure()
        