import random

class RandomWalk:
    def __init__(self):
        SIMULATIONS = 10000

        for lattice in range(10, 81):
            dead_end_count = 0
            for _ in range(SIMULATIONS):
                self.iteration = lattice
                self.pos = [[0, 0]]
                self.current_pos = Position(0, 0)
                self.heading = 90
                exceed, collision = False, False

                while not (exceed or collision):
                    direction = random.randint(1, 3)
                    #left
                    if direction == 2:
                        self.heading = self.heading - 90 if self.heading >= 90 else 270
                    #right
                    elif direction == 3:
                        self.heading = self.heading + 90 if self.heading < 270 else 0

                    if self.heading == 0:
                        self.current_pos.y += 1
                    elif self.heading == 90:
                        self.current_pos.x += 1
                    elif self.heading == 180:
                        self.current_pos.y -= 1
                    elif self.heading == 270:
                        self.current_pos.x -= 1

                    exceed = self.exceed_border()
                    collision = self.collision()

                if collision:
                    dead_end_count += 1
            print(f"For a lattice size of {lattice}, the probability of dead-end paths is {(dead_end_count / SIMULATIONS) * 100:.1f}%")

    def exceed_border(self):
        if not int(-self.iteration / 2) <= self.current_pos.x <= int(self.iteration / 2):
            return True
        if not int(-self.iteration / 2) <= self.current_pos.y <= int(self.iteration / 2):
            return True
        return False

    def collision(self):
        if [self.current_pos.x, self.current_pos.y] not in self.pos:
            self.pos.append([self.current_pos.x, self.current_pos.y])
        else:
            return True
        return False

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

RandomWalk()
