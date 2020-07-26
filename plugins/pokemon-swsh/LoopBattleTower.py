import logging
from JoycontrolPlugin import JoycontrolPlugin

logger = logging.getLogger(__name__)

class LoopBattleTower(JoycontrolPlugin):
    async def loop_battle_tower(self):
        '''
        Commands:
          AA (wait 17sec) AA UP AA UP AAA (wait 17sec) AABB UP
        Rental Team ID:
          0000-0006-15Y4-3R
        References:
          - https://twitter.com/satoon_sugar/status/1208248084653674496
          - https://twitter.com/satoon_sugar/status/1208253657470226432
        '''

        command_list = [
            'a', 'a', 'wait',
            'a', 'a', 'up',
            'a', 'a', 'up',
            'a', 'a', 'a', 'wait',
            'a', 'a', 'b', 'b', 'up',
        ]

        i = 0
        while True:
            cmd = command_list[i % len(command_list)]
            logger.info(f'Command: {cmd}')
            if cmd == 'wait':
                await self.wait(16.2)
            else:
                await self.button_push(cmd)
                await self.wait(0.8)
            i += 1

    async def run(self):
        logger.info('Loop Battle Tower Plugin loaded!')
        await self.loop_battle_tower()
