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
    if angle < 360 and angle > 180:
        apt = 10*np.sin(np.deg2rad(angle))
        #print "\nRIGHT APT\n", apt
        return apt
    return 0

def left(angle):
    if angle > 0 and angle < 180:
        apt = -10*np.sin(np.deg2rad(angle))
        #print "\nLEFT APT\n", apt
        return apt
    return 0

def lost(angle):
    if 90 < angle and angle < 270:
        apt = 10*np.cos(np.deg2rad(angle))
        #print "\nLOST APT\n", apt
        return apt
    else:
        return 0

def move_Horn(distance):
    #if close and mid, then move is low
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
    angle %= 360
    #print "\nANGLE \n", angle
    right_or_right = min(right(angle), left(angle))
    lost_or_left = min(lost(angle), left(angle))
    lost_or_right = min(lost(angle), right(angle))
    apt = (120*(right_or_right+lost_or_left+lost_or_right))/360
    if angle < 180:
        apt = apt
    else:
        apt = -apt
    return apt
