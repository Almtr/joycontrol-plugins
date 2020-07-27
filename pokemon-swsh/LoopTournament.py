import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class LoopTournament(JoycontrolPlugin):
    async def loop_tournament(self):
        '''
        Commands:
          Button: AA ... AAB
          Stick:  Slightly Upper Right
        Reference:
          http://niwaka-syndrome.blog.jp/archives/20509394.html
        '''

        # Slightly Upper Right
        await self.left_stick(angle=110)

        while True:
            for _ in range(10):
                await self.button_push('a')
                await self.wait(0.5)

            # Select B button occasionally
            await self.button_push('b')
            await self.wait(0.5)

        # Reset left stick position
        await self.left_stick('center')
        await self.wait(0.5)

    async def run(self):
        logger.info('Loop Tournament Plugin loaded!')
        await self.loop_tournament()
