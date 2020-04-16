import math
from time import sleep


class FakeRobot:
    speed = 50
    position = (0, 0, 0)
    positions = [(0, 0, 0)]
    _heading = 0

    sleep(0)

    def __init__(self):
        """ Constructor for this class. """
        # do nothing

    def set_heading(self, angle):
        """Add angle to the current heading of the robot"""
        self._heading = angle

    def turn(self, angle):
        """Add angle to the current heading of the robot"""
        self.set_heading(self._heading + angle)

    def forward(self, distance):
        i = 0

        while True:
            sleep(1 * 0.01)
            i = i + 1
            if i * self.speed * 0.01 >= distance:
                break

        self.position = (
            self.position[0] + round(math.cos(math.radians(self._heading)) * distance, 2),
            self.position[1] + round(math.sin(math.radians(self._heading)) * distance, 2),
            self._heading
        )

        print(self.position)

        self.positions.append(self.position)

    def backward(self, distance):
        i = 0
        while True:
            sleep(1 * 0.01)
            i = i + 1
            if i * self.speed * 0.01 >= distance:
                break

        self.position = (
            self.position[0] - round(math.cos(math.radians(self._heading)) * distance, 2),
            self.position[1] - round(math.sin(math.radians(self._heading)) * distance, 2),
            self._heading
        )

        print(self.position)

        self.positions.append(self.position)
