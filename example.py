#!/usr/bin/env python
# -*- coding: utf-8 -*-

from FakeRobot import FakeRobot

robot = FakeRobot()

robot.speed = 2

robot.turn(45)

robot.forward(2)

robot.turn(45)

robot.backward(2)

print(robot.positions)
