import numpy as np
from math import *

def far(distance):
    if distace > 340:
        return 2*distance - 740
    else:
        return 0

def close(distance):
    if distace < 340:
        return -2*distance + 740
    else:
        return 0

def mid(distance):
    if distace < 340:
        return 2*distance
    else:
        return -2*distance -1440

def north(angle):
    if angle > 20 and angle < 180:
        rads = deg2rad(angle)
        return sen(rads)
    else:
        return 0

def south(angle):
    if angle > 200 and angle < 340:
        rads = deg2rad(angle)
        return sen(rads)
    else:
        return 0

def east(angle):
    if angle < 70 or angle > 290:
        rads = deg2rad(angle)
        return cos(rads)
    else:
        return 0

def west(angle):
    if angle < 250 and angle > 110:
        rads = deg2rad(angle)
        return cos(rads)
    else:
        return 0
