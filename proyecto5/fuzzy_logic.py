import numpy as np
from math import *

def far(distance):
    if (distance < 740 and distance > 370):
        #print "far"
        return (distance/370)-1
    return 0

def close(distance):
    if (distance > 0 and distance < 370):
        #print "close"
        return -(distance/370)+1
    return 0

def mid(distance):
    if (distance > 0 and distance < 370):
        #print "mid1"
        return distance/370
    if (distance < 740 and distance > 370):
        #print "mid2"
        return -(distance/370)+2
    return 0

def right(angle):
    if angle < 100:
        return np.cos(np.deg2rad(angle))
    return 0

def left(angle):
    if angle < 360 and angle > 260:
        return np.cos(np.deg2rad(angle))
    return 0

def lost(angle):
    if 100 > angle and angle < 260:
        return 0
    else:
        return np.sin(np.deg2rad(angle))

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
    #print "top_of_low_movement", top_of_low_movement
    #print "top_of_mid_movement", top_of_mid_movement
    #print "top_of_high_movement", top_of_high_movement
    #print "Movement per time ", mpt
    return 10*mpt


def view_Horn(angle):
    #if close and mid, then move is low
    print "Angle", angle
    top_of_left = min(left(angle), lost(angle))
    #if mid, then move is mid
    top_of_right = min(right(angle), lost(angle))
    #if mid, then move is mid
    top_of_lost = min(lost(angle), min(right(angle), left(angle)))
    #max movement will be 24 units per time, so there is 8 units per function
    apt = (120*(top_of_left+top_of_right+top_of_lost))/360
    #print "top_of_left", top_of_left
    #print "top_of_right", top_of_right
    print "top_of_lost", top_of_lost
    print "Angle change per time ", apt
    return 10*apt
