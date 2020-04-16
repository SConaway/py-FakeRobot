#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Import FakeRobot
from FakeRobot import FakeRobot

# Create Robot
robot = FakeRobot()

# Set speed of robot. Speed is between 1 and 100
robot.speed = 2

# Turn robot by x degrees.
robot.turn(45)
# Alternatively,
# robot.set_heading(-34)
# to set an absolute heading

# Move the robot forward x units
robot.forward(2)

# Turn robot by x degrees.
robot.turn(45)
# Alternatively,
# robot.set_heading(-34)
# to set an absolute heading

# Move the robot backward x units
robot.backward(2)

# Print a list of all its positions
print(robot.positions)
