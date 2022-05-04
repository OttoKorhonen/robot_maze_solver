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
    def change_direction(self, direction:str):
        if direction == 'up':
            self.direction = 'right'
        if direction == 'right':
            self.direction = 'down'
        if direction == 'down':
            self.direction = 'left'
        if direction == 'left':
            self.direction = 'up'

    # funktio etsii kartasta aloituspaikan ja palauttaa sen tuplena
    def find_start(self):
        map = self.read_map()
        try:
            for line in map:
                for marking in line:
                    if marking == 'S':
                        self.position = map.index(line), line.index(marking)
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
                        return map.index(line), line.index(marking)
        except:
            raise ValueError('Exit could not be found')

    def count_steps(self):
        self.steps = self.steps + 1

    def take_step(self, direction: str):
        if direction == 'up':
            y = list(self.position)
            y[0] = self.position[0] - 1
            self.position = tuple(y)
        if direction == 'right':
            x = list(self.position)
            x[1] = self.position[1] + 1
            self.position = tuple(x)
        if direction == 'down':
            y = list(self.position)
            y[0] = self.position[0] + 1
            self.position = tuple(y)
        if direction == 'left':
            x = list(self.position)
            x[1] = self.position[1] - 1
            self.position = tuple(x)

    
    def hash(self, map:str):
        position = self.position
        if self.direction == 'up' and map[position[0]-1][position[1]] == '#' or self.direction == 'right' and map[position[0]][position[1]+1] == '#' or self.direction == 'down' and map[position[0]+1][position[1]] == '#' or self.direction == 'left' and map[position[0]][position[1]-1] == '#':
            return True


    def get_out(self):
        start = self.find_start()
        map = self.read_map()
        self.tile = map[start[0]][start[1]]
        exit = self.find_exit()
        
        while True:
            sleep(0.1)
            print(self, exit)
            self.take_step(self.direction)
            self.count_steps()
            if self.hash(map):
                self.change_direction(self.direction)
            # if self.tile == '#':
            #     self.change_direction(self.direction)
                
            if self.tile == 'E':
                break
            # if self.position == self.find_exit:
            #     print(self.steps)
            #     break
                

            self.tile = map[self.position[0]][self.position[1]]
        
        print(f'Robotin askeleet: {self.steps}')
        return self.steps

if __name__ == '__main__':
    robot = Robot('map_4597926.txt')
    #robot = Robot('map_4159889.txt')
    #robot = Robot('map_2701837.txt')
    #robot = Robot('test_map.txt')
    robot.get_out()
