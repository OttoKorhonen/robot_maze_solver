from time import sleep


class Robot():

    def __init__(self, map: str):
        self.steps = 0
        self.map = map
        self.position = ()
        self.tile = ''
        self.direction = 'up'

    def __str__(self):
        return f'Robot data:\nsteps: {self.steps}, direction: {self.direction}, position: {self.position}, tile: {self.tile}'

    # funktio lukee karttatiedoston, tekee kartasta kaksiulotteisen listan ja palauttaa sen
    def read_map(self):
        with open(self.map, 'r') as map:
            map = map.readlines()

        return [list(mark.strip()) for mark in map]

    def mark_path(self):
        with open('marked_map.txt', 'w') as map:
            map = map.write()

    # muuttaa robotin kulkemaa suuntaa
    def change_direction(self, direction: str):
        if direction == 'up':
            self.direction = 'right'
        elif direction == 'right':
            self.direction = 'down'
        elif direction == 'down':
            self.direction = 'left'
        elif direction == 'left':
            self.direction = 'up'

    # funktio etsii kartasta aloituspaikan ja palauttaa sen tuplena
    def find_start(self):
        map = self.read_map()
        try:
            for line in map:
                for marking in line:
                    if marking == 'S':
                        self.position = map.index(line), line.index(marking)
                        print('Position located!')
                        return map.index(line), line.index(marking)
        except:
            raise ValueError('Start position could not be found')

    # funktio etsii kartasta ulospääsypaikan ja palauttaa sen tuplena
    def find_exit(self):
        map = self.read_map()
        try:
            for line in map:
                for marking in line:
                    if marking == 'E':
                        print('Exit located!')
                        return map.index(line), line.index(marking)
        except:
            raise ValueError('Exit could not be found')

    def count_steps(self):
        self.steps += 1

    def take_step(self, direction: str, map):
        y, x, obj = self.move_to(direction, map)

        if obj != '#':
            self.tile = map[y][x]
            self.position = y, x
            self.count_steps()
        else:
            self.change_direction(direction)

    def move_to(self, direction: str, map):
        y, x = self.position

        if direction == 'up':
            y -= 1
        elif direction == 'down':
            y += 1
        elif direction == 'left':
            x -= 1
        elif direction == 'right':
            x += 1
        else:
            raise ValueError(f'Direction error: Direction {direction}')

        return y, x, map[y][x]

    def get_out(self):
        start_x, start_y = self.find_start()
        map = self.read_map()
        self.tile = map[start_x][start_y]
        self.find_exit()

        print('Processing...(🤖)')

        while True:
            sleep(0.1)
            self.take_step(self.direction, map)

            if self.tile == 'E':
                break

        print(f'It took {self.steps} for the (🤖) to get out')
        return self.steps


if __name__ == '__main__':
    robot = Robot('map_1637284.txt')
    #robot = Robot('map_4597926.txt')
    #robot = Robot('map_4159889.txt')
    #robot = Robot('map_2701837.txt')
    #robot = Robot('test_map.txt')
    robot.get_out()
