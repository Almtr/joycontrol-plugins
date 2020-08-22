import logging
import itertools
from JoycontrolPlugin import JoycontrolPlugin, JoycontrolPluginError

logger = logging.getLogger(__name__)

class Keypad:
    def __init__(self):
        self.keypad = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9],
            [-1,0,-1],
        ]


    def __num2pos(self, num: int):
        max_x = len(self.keypad[0])
        max_y = len(self.keypad)
        for x, y in itertools.product(range(max_x), range(max_y)):
            if self.keypad[y][x] == num:
                return {'x':x, 'y':y}
        return None


    def shortest_path(self, current_num: int, target_num: int):
        current_pos = self.__num2pos(current_num)
        target_pos = self.__num2pos(target_num)
        max_x = len(self.keypad[0])
        max_y = len(self.keypad)

        path = []
        while True:
            x = current_pos['x']
            y = current_pos['y']
            diff_x = target_pos['x'] - current_pos['x']
            diff_y = target_pos['y'] - current_pos['y']

            if diff_x == diff_y == 0:
                break

            if   diff_x > 0 and 0 <= x+1 < max_x and self.keypad[y][x+1] != -1:
                path.append('right')
                current_pos['x'] += 1
            elif diff_x < 0 and 0 <= x-1 < max_x and self.keypad[y][x-1] != -1:
                path.append('left')
                current_pos['x'] -= 1
            elif diff_y > 0 and 0 <= y+1 < max_y and self.keypad[y+1][x] != -1:
                path.append('down')
                current_pos['y'] += 1
            elif diff_y < 0 and 0 <= y-1 < max_y and self.keypad[y-1][x] != -1:
                path.append('up')
                current_pos['y'] -= 1
        return path


class DistributeRaid(JoycontrolPlugin):
    def __init__(self, controller_state, options):
        super().__init__(controller_state, options)

        usage = 'Please use "--plugin-options <link_code> [backup]".'

        if options is None:
            raise JoycontrolPluginError(f'Plugin option is not set. {usage}')

        self.link_code = options[0] # require option
        self.backup_mode = False # default

        if not self.link_code.isdecimal() or len(self.link_code) != 8:
            raise ValueError(f'Invalid link code ({self.link_code}). {usage}')

        if len(options) >= 2:
            if options[1] != 'backup':
                raise ValueError(f'Invalid backup mode ({options[1]}). {usage}')
            self.backup_mode = True


    async def push_linkcode(self, link_code):
        keypad = Keypad()
        current_num = 1 # init position

        for num in link_code:
            target_num = int(num)
            path = keypad.shortest_path(current_num, target_num)
            current_num = target_num

            # Move to target number
            for button in path:
                await self.button_push(button)
                await self.wait(0.5)
            
            # Push a number
            await self.button_push('a')
            await self.wait(0.5)


    async def distribute_raid(self):
        count = 0
        while True:
            # Start the game
            await self.button_push('a')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(20)

            if self.backup_mode:
                # Boot from backup
                await self.button_push('up' , 'x', 'b')
                await self.wait(3)
                await self.button_push('a')
                await self.wait(2)

            await self.button_push('a')
            await self.wait(10)

            # Connect to the Internet
            await self.button_push('y')
            await self.wait(1)
            await self.button_push('plus')
            await self.wait(20)
            await self.button_push('b')
            await self.wait(0.5)
            await self.button_push('b')
            await self.wait(0.5)

            # Examine a den
            await self.button_push('a')
            await self.wait(4)

            # Set the link code
            await self.button_push('plus')
            await self.wait(1)
            await self.push_linkcode(self.link_code)  
            await self.button_push('plus')
            await self.wait(1)
            await self.button_push('a')
            await self.wait(1)

            # Waiting for connection
            await self.button_push('a')
            await self.wait(60)

            # Start the battle
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

            # Exit the game
            await self.button_push('home')
            await self.wait(1.5)
            await self.button_push('x')
            await self.wait(0.5)
            await self.button_push('a')
            await self.wait(5)

            count += 1
            logger.info(str(count) + 'cycle finished.')        
       
       
    async def run(self):
        logger.info('Distribute Raid Plugin loaded!')
        await self.distribute_raid()