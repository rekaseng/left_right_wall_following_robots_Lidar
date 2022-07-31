#!/usr/bin/env python3
from eye import *
import random

SPEED = 200
ASPEED = 100
THRES = 220


DISTANCE = 25
DEGREE_TO_TURN = 90

DEGREE_TO_CURVE = int(DEGREE_TO_TURN / 2)


def turn_left():
    VWTurn(DEGREE_TO_TURN, ASPEED)  # turn
    VWWait()


def curve_left():
    VWCurve(DISTANCE, DEGREE_TO_CURVE, SPEED)
    VWWait()


def turn_right():
    VWTurn(-DEGREE_TO_TURN, ASPEED)  # turn
    VWWait()


def curve_right():
    VWCurve(DISTANCE, -DEGREE_TO_CURVE, SPEED)
    VWWait()


def straight():
    VWStraight(DISTANCE, SPEED)  # go one step
    VWWait()


def main():
    LCDPrintf("My MAZE Left\n")
    LCDMenu("", "", "", "END")
    while KEYRead() != KEY4:
        front = int(PSDGet(PSD_FRONT) > THRES)
        left = int(PSDGet(PSD_LEFT) > THRES)
        right = int(PSDGet(PSD_RIGHT) > THRES)
        # Drive right when possible, if not straight, if not right, else turn 180
        # .....
        front_half = int(PSDGet(PSD_FRONT) < THRES / 2)
        left_half = int(PSDGet(PSD_LEFT) < THRES / 2)
        right_half = int(PSDGet(PSD_RIGHT) < THRES / 2)

        if right == 1:
            LCDPrintf("RIGHT is SAFE, now turning left\n")
            curve_right()

            if front == 1:
                LCDPrintf("FRONT is SAFE, now moving forward\n")
                straight()
        elif front == 1:
            LCDPrintf("RIGHT is NOT safe, checking front\n")
            LCDPrintf("FRONT is SAFE, now moving forward\n")
            straight()

        elif left == 1:
            LCDPrintf("LEFT and FRONT are NOT safe, checking right\n")
            LCDPrintf("LEFT is SAFE, now turning right\n")
            turn_left()
            if front == 1:
                LCDPrintf("FRONT is SAFE, now moving forward\n")
                straight()  # front is also safe, now move forward

        else:
            LCDPrintf("LEFT, FRONT and RIGHT are NOT safe, turning back on the spot\n")
            turn_left()  # all are not safe, now turning around
            turn_left()  # to achieve 180 turn around

        if left_half == 1:
            curve_right()
        if right_half == 1:
            curve_left()
        if front_half == 1:
            turn_right()
            turn_right()

    return 0


if _name_ == "_main_":
    main()
# This program is just randomly drive
# TODO: Create new or modify this program so that it is RIGHT wall-following program
# You are ALLOWED to refer to ANY references
