import numpy as np
from math import *

def far(distance):
    if (distance < 740 and distance > 370):
        print "far"
        return (distance/370)-1
    return 0

def close(distance):
    if (distance > 0 and distance < 370):
        print "close"
        return -(distance/370)+1
    return 0

def mid(distance):
    if (distance > 0 and distance < 370):
        print "mid1"
        return distance/370
    if (distance < 740 and distance > 370):
        print "mid2"
        return -(distance/370)+2
    return 0

def north(angle):
    if angle > 20 and angle < 180:
        rads = deg2rad(angle)
        return sen(rads)
    else:
        return 0

def left(angle):
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
    return 5*mpt
