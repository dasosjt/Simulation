import numpy as np
from math import *

def far(distance):
    if distance < 740 and distance > 320:
        return (2*distance - 740)/740
    else:
        return 0

def close(distance):
    if distance > 0 and distance < 320:
        return (-2*distance + 740)/740
    else:
        return 0

def mid(distance):
    if distance > 0 and distance < 320:
        return (2*distance)/740
    elif distance < 740:
        return (-2*distance -1480)/740
    return 0
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

def move_Horn(distance):
    #if close and mid, then move is low
    print "Distance", distance
    top_of_low_movement = min(close(distance), mid(distance))
    #if mid, then move is mid
    top_of_mid_movement = mid(distance)
    #if mid, then move is mid
    top_of_high_movement = min(far(distance), mid(distance))
    #max movement will be 24 units per time, so there is 8 units per function
    mpt = (8*(top_of_low_movement+top_of_mid_movement+top_of_high_movement))/24
    print "top_of_low_movement", top_of_low_movement
    print "top_of_mid_movement", top_of_mid_movement
    print "top_of_high_movement", top_of_high_movement
    print "Movement per time ", mpt
    return mpt
