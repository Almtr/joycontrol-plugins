import itertools

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