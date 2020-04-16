import math
from time import sleep


class FakeRobot:
    speed = 1
    position = (0, 0, 0)
    positions = [(0, 0, 0)]
    heading = 0

    sleep(0)

    def __init__(self):
        """ Constructor for this class. """
        # do nothing

    def turn(self, angle):
        self.heading += angle

    def forward(self, distance):
        i = 0

        while True:
            # sleep(1 * 0.01)
            i = i + 1
            if i * self.speed * 0.01 >= distance:
                break

        self.position = (
            self.position[0] + round(math.cos(math.radians(self.heading)) * distance, 2),
            self.position[1] + round(math.sin(math.radians(self.heading)) * distance, 2),
            self.heading
        )

        print(self.position)

        self.positions.append(self.position)

    def backward(self, distance):
        i = 0
        while True:
            # sleep(1 * 0.01)
            i = i + 1
            if i * self.speed * 0.01 >= distance:
                break

        self.position = (
            self.position[0] - round(math.cos(math.radians(self.heading)) * distance, 2),
            self.position[1] - round(math.sin(math.radians(self.heading)) * distance, 2),
            self.heading
        )

        print(self.position)

        self.positions.append(self.position)
