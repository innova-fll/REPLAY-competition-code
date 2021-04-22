#!/usr/bin/env python3
from ev3dev2.motor import *
import time
from ev3dev2.sensor.lego import *
from ev3dev2.sensor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
import multiprocessing


# Declare motors
motor_right = Motor(OUTPUT_A)
motor_left = Motor(OUTPUT_D)
medium_up_down = Motor(OUTPUT_C)
medium_left_right = Motor(OUTPUT_B)
tank_pair = MoveTank(OUTPUT_A, OUTPUT_D)
gyro = GyroSensor(INPUT_3)
color_left = ColorSensor(INPUT_1)
color_right = ColorSensor(INPUT_2)

#D is left
#C is up and down

button = Button()

medium_up_down_speed = 1000
medium_left_right_speed = 1000

for x in range(10):
    print('DONE LOADING')


def stop():
    motor_right.stop()
    motor_left.stop()
    medium_up_down.stop()
    medium_left_right.stop()
    tank_pair.stop()


def run1():
    initial_angle = gyro.angle

    #----Wall Reset----#
    # Wall Right
    medium_left_right.run_forever(speed_sp=-medium_left_right_speed)
    time.sleep(1.25)
    medium_left_right.stop()

    # Wall Left
    medium_left_right.run_forever(speed_sp=medium_left_right_speed)
    time.sleep(0.25)
    medium_left_right.stop()

    time.sleep(3)

    # Wall Down
    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(0.55)
    medium_up_down.stop()

    # Wall up
    medium_up_down.run_forever(speed_sp=-medium_up_down_speed)
    time.sleep(0.75)
    medium_up_down.stop()
    #----Getting to the bench----#

    # Move Forward
    motor_left.run_forever(speed_sp=-400)
    motor_right.run_forever(speed_sp=-400)
    time.sleep(2.4)
    motor_right.stop()
    motor_left.stop()

    #----Lifting off the backrest and pushing down the bench----#

    # Lifting up one side of backrest
    medium_up_down.run_forever(speed_sp=-medium_up_down_speed)
    time.sleep(1)
    medium_up_down.stop()

    # Turn Left to use the other end of the backrest that's still in to push the bench a bit
    motor_left.run_forever(speed_sp=250)
    motor_right.run_forever(speed_sp=-250)
    time.sleep(0.2)
    motor_right.stop()
    motor_left.stop()

    # Turn to yoink the other end of the backrest off.
    motor_left.run_forever(speed_sp=200)
    motor_right.run_forever(speed_sp=-200)
    time.sleep(1)
    motor_right.stop()
    motor_left.stop()

    #----Putting the cubes in----#

    # Gyro Turn Right to be alligned.
    while gyro.angle < initial_angle + 5:
        motor_left.run_forever(speed_sp=-300)
        motor_right.run_forever(speed_sp=300)

    # Move forward a bit for extra accuracy
    motor_left.run_forever(speed_sp=-250)
    motor_right.run_forever(speed_sp=-250)
    time.sleep(0.85)

    motor_left.stop()
    motor_right.stop()

    # Lowering wall a bit
    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(0.75)
    medium_up_down.stop()

    # Wall Right to drop the cubes
    medium_left_right.run_forever(speed_sp=-medium_left_right_speed)
    time.sleep(0.5)
    medium_left_right.stop()

    # Move Backwards to push in any remaining cubes at the front of the bench
    motor_left.run_forever(speed_sp=100)
    motor_right.run_forever(speed_sp=100)
    time.sleep(1.25)
    motor_left.stop()
    motor_right.stop()

    #----Going back to base----#

    # Moving wall up to not get in the way of the cubes
    medium_up_down.run_forever(speed_sp=-medium_up_down_speed)
    time.sleep(0.3)
    medium_up_down.stop()

    # Move Backwards back to base
    motor_left.run_forever(speed_sp=400)
    motor_right.run_forever(speed_sp=800)
    time.sleep(3)
    motor_left.stop()
    motor_right.stop()

    #----END----#


def run2():
    initial_angle = gyro.angle

    #----Wall Reset----#

    # Wall Up
    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(0.75)
    medium_up_down.stop()

    # Wall Right
    medium_left_right.run_forever(speed_sp=-medium_left_right_speed)
    time.sleep(1)
    medium_left_right.stop()

    #----Go to bench----#

    # Move Forward
    motor_left.run_forever(speed_sp=-300)
    motor_right.run_forever(speed_sp=-300)
    time.sleep(3.25)
    motor_left.stop()
    motor_right.stop()

    #----Drop off the innovation project----#

    # Wall Up
    medium_up_down.run_forever(speed_sp=-medium_up_down_speed)
    time.sleep(0.75)
    medium_up_down.stop()

    #----Move away and turn to the slide----#

    # Move Back
    motor_left.run_forever(speed_sp=300)
    motor_right.run_forever(speed_sp=300)
    medium_up_down.run_forever(speed_sp=(medium_up_down_speed/10))
    time.sleep(1.6)
    motor_left.stop()
    motor_right.stop()
    medium_up_down.stop()

    time.sleep(0.5)

    # Turn to slide

    while gyro.angle < initial_angle + 54:
        motor_left.run_forever(speed_sp=-100)
        motor_right.run_forever(speed_sp=100)

    while gyro.angle > initial_angle + 54:
        motor_left.run_forever(speed_sp=50)
        motor_right.run_forever(speed_sp=-50)

    motor_left.stop()
    motor_right.stop()

    #----Prepare for the slide----#

    # Wall Down
    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(0.25)
    medium_up_down.stop()

    #----Go to slide----#

    # Move Forward
    motor_left.run_forever(speed_sp=-500)
    motor_right.run_forever(speed_sp=-500)
    time.sleep(2.3)
    motor_left.stop()
    motor_right.stop()

    # Move Forward
    motor_left.run_forever(speed_sp=-250)
    motor_right.run_forever(speed_sp=-250)
    time.sleep(1)
    motor_left.stop()
    motor_right.stop()

    #----Push person off the slide----#

    # Go backwards
    motor_left.run_forever(speed_sp=200)
    motor_right.run_forever(speed_sp=200)
    time.sleep(0.75)
    motor_left.stop()
    motor_right.stop()

    # Wait for person a little bit
    time.sleep(1)

    #----Head back to base----#

    motor_left.run_forever(speed_sp=150)
    motor_right.run_forever(speed_sp=150)
    time.sleep(0.25)
    motor_left.stop()
    motor_right.stop()

    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(0.1)
    medium_up_down.stop()

    motor_left.run_forever(speed_sp=300)
    motor_right.run_forever(speed_sp=300)
    time.sleep(0.375)
    motor_left.stop()
    motor_right.stop()

    motor_left.run_forever(speed_sp=500)
    motor_right.run_forever(speed_sp=400)
    time.sleep(1)
    motor_left.stop()
    motor_right.stop()

    # Wall Left
    medium_left_right.run_forever(speed_sp=medium_left_right_speed)
    time.sleep(0.35)
    medium_left_right.stop()

    motor_left.run_forever(speed_sp=450)
    motor_right.run_forever(speed_sp=600)
    time.sleep(3)
    motor_left.stop()
    motor_right.stop()


def run3():
    sound = Sound()
    initial_angle = gyro.angle

    def stoplr():
        motor_right.stop()
        motor_left.stop()

    def stopatline_r():
        while color_right.reflected_light_intensity > 15:
            motor_right.run_forever(speed_sp=-250)
            motor_left.run_forever(speed_sp=-250)
        stoplr()

    def stopatline_l():
        while color_left.reflected_light_intensity > 15:
            motor_right.run_forever(speed_sp=-250)
            motor_left.run_forever(speed_sp=-250)
        stoplr()

    def antibump(ang, speed):
        gything = gyro.angle - ang
        motor_left.run_forever(speed_sp=speed - gything)
        motor_right.run_forever(speed_sp=speed + gything)

    # ---- Resets wall ---- #
    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(0.8)
    medium_up_down.stop()

    # ---- Pushes the Step Counter ---- #
    motor_left.run_forever(speed_sp=-600)
    motor_right.run_forever(speed_sp=-550)
    time.sleep(3.5)
    stoplr()

    # turn slightly to the right while moving to not hit the lock on the step counter
    motor_right.run_forever(speed_sp=-350)  # was 200
    motor_left.run_forever(speed_sp=-300)
    time.sleep(1)

    # go straight to now push the lock to keep it in place
    motor_right.run_forever(speed_sp=-300)  # was 200
    motor_left.run_forever(speed_sp=-300)
    time.sleep(2)

    # slowly go back
    motor_right.run_forever(speed_sp=250)
    motor_left.run_forever(speed_sp=250)
    time.sleep(.5)
    stoplr()

    # turn right while backing up
    motor_right.run_forever(speed_sp=200)
    motor_left.run_forever(speed_sp=100)
    time.sleep(4.2)
    stoplr()
    initial_angle

    # Turn to weight machiene

    # Gyro turn to face the weight machiene
    while gyro.angle > initial_angle + 1:
        motor_right.run_forever(speed_sp=-150)
        motor_left.run_forever(speed_sp=150)
    stoplr()

    # Extra gyro turn for extra accuracy
    while gyro.angle < initial_angle + 1:
        motor_right.run_forever(speed_sp=50)
        motor_left.run_forever(speed_sp=-50)
    stoplr()

    # ---- Moves toward weight machine ---- #

    # Gyro straight while wall goes down
    antibump(initial_angle, -500)
    medium_up_down.run_forever(speed_sp=-medium_up_down_speed)
    time.sleep(3.5)

    # ---- Stops at the line next to the weight machine ---- #
    stopatline_l()
    medium_up_down.stop()

    # ---- Aligning to wall ---- #

    # Gyro turn to have back face wall
    old_gyro_angle = gyro.angle
    while gyro.angle > old_gyro_angle - 88:
        motor_left.run_forever(speed_sp=100)
        motor_right.run_forever(speed_sp=-100)
    stoplr()

    while gyro.angle < old_gyro_angle - 92:
        motor_right.run_forever(speed_sp=50)
        motor_left.run_forever(speed_sp=-50)
    stoplr()

    # Go back into wall to allign
    motor_right.run_forever(speed_sp=250)
    motor_left.run_forever(speed_sp=250)
    time.sleep(1)
    stoplr()

    # wait a little so there's no jerk
    time.sleep(1)

    # Move forward to weight machiene
    motor_right.run_forever(speed_sp=-250)
    motor_left.run_forever(speed_sp=-250)
    time.sleep(2.1)
    stoplr()

    # ---- Moves wall up ---- #
    medium_up_down.run_forever(speed_sp=-medium_up_down_speed)
    time.sleep(1.5)
    medium_up_down.stop()

    # ---- Turns, moves back a bit, and puts axel(s) in weight machiene tire ---- #

    old_gyro_angle = gyro.angle

    while gyro.angle < old_gyro_angle + 65:
        motor_left.run_forever(speed_sp=-200)
        motor_right.run_forever(speed_sp=200)
    stoplr()

    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(1.2)
    medium_up_down.stop()

    # ---- Pulling weight machiene tire to circle ---- #
    old_gyro_angle = gyro.angle

    while gyro.angle > old_gyro_angle - 40:
        motor_right.run_forever(speed_sp=-100)
        motor_left.run_forever(speed_sp=100)
    stoplr()

    motor_left.run_forever(speed_sp=50)
    motor_right.run_forever(speed_sp=50)
    time.sleep(1.6)
    stoplr()

    # ---- Moves wall up ---- #
    medium_up_down.run_forever(speed_sp=-medium_up_down_speed)
    time.sleep(2.75)
    medium_up_down.stop()

    # ---- Moves and turns toward large blue tire ---- #
    old_gyro_angle = gyro.angle

    while gyro.angle > old_gyro_angle - 85:
        motor_right.run_forever(speed_sp=-100)
        motor_left.run_forever(speed_sp=100)
    stoplr()

    motor_right.run_forever(speed_sp=-250)
    motor_left.run_forever(speed_sp=-250)
    time.sleep(1.35)
    stoplr()

    # ---- Puts axles in large blue tire ---- #
    medium_up_down.run_forever(speed_sp=medium_up_down_speed)
    time.sleep(1.2)
    medium_up_down.stop()

    motor_right.run_forever(speed_sp=-500)
    motor_left.run_forever(speed_sp=500)
    time.sleep(.1)

    motor_right.run_forever(speed_sp=500)
    motor_left.run_forever(speed_sp=-500)
    time.sleep(.1)

    motor_right.run_forever(speed_sp=-500)
    motor_left.run_forever(speed_sp=500)
    time.sleep(.1)

    # ---- Turns toward home/base ---- #
    old_gyro_angle = gyro.angle

    while gyro.angle > old_gyro_angle - 40:
        motor_right.run_forever(speed_sp=-100)
        motor_left.run_forever(speed_sp=100)
    stoplr()

    # ---- Moves forward a bit ---- #
    motor_left.run_forever(speed_sp=-250)
    motor_right.run_forever(speed_sp=-250)
    time.sleep(2)
    stoplr()

    # ---- Turns toward home/base ---- #
    old_gyro_angle = gyro.angle

    while gyro.angle < old_gyro_angle + 15:
        motor_left.run_forever(speed_sp=-200)
        motor_right.run_forever(speed_sp=200)
    stoplr()

    while gyro.angle > old_gyro_angle + 50:
        motor_left.run_forever(speed_sp=50)
        motor_right.run_forever(speed_sp=-50)
    stoplr()

    # ---- Moves toward home/base ---- #
    motor_right.run_forever(speed_sp=-500)
    motor_left.run_forever(speed_sp=-500)
    time.sleep(1)

    motor_right.run_forever(speed_sp=-1000)
    motor_left.run_forever(speed_sp=-1000)
    time.sleep(7)

    # ---- Teh end of teh ting ---- #


def run4():
    angle = gyro.angle
    # wall down
    medium_up_down.on_for_seconds((medium_up_down_speed/10), 10)
    # move forward
    tank_pair.on_for_seconds(-50, -50, 4.2)
    time.sleep(1)
    while(True):
        # turning left to go through pull up bar
        motor_left.on(40)
        if gyro.angle - angle <= -70:
            motor_left.stop()
            break
    tank_pair.on_for_seconds(-30, -30, 1)
    # follow line
    while(True):
        # go through pull up bar
        if color_right.color == 3:
            tank_pair.on(-5, -25)
        elif color_right.color == 1:
            tank_pair.on(-25, -5)
        elif color_right.color == 6:
            tank_pair.on(-5, -25)
        if color_left.color == 1:
            tank_pair.stop()
            break
    time.sleep(1)
    # realign to put cubes into area
    while(True):
        motor_left.on(20)
        if gyro.angle - angle <= -90:
            motor_left.stop()
            break
    while(True):
        motor_left.on(-10)
        if gyro.angle - angle >= -90:
            motor_left.stop()
            break
    tank_pair.on_for_seconds(-35, -35, 1.25)
    # lift wall
    medium_up_down.on_for_seconds((-medium_up_down_speed/20), 1000)
    time.sleep(0.5)
    # shake
    medium_up_down.on_for_seconds((medium_up_down_speed/10), 1000)

    tank_pair.on_for_seconds(35, 35, 0.25)
    # put yellow cube into area
    motor_right.on(100)
    gyro.wait_until_angle_changed_by(35)
    motor_right.stop()
    tank_pair.on_for_seconds(-25, -25, 1)
    # wall up to lift lever
    medium_up_down.on_for_seconds((-medium_up_down_speed/10), 1000)
    # realign for dance floor
    time.sleep(0.5)
    motor_left.on(100)
    gyro.wait_until_angle_changed_by(90)
    motor_left.stop()
    tank_pair.on_for_seconds(-50, -50, 2)
    motor_right.on(100)
    gyro.wait_until_angle_changed_by(35)
    motor_right.stop()
    tank_pair.on_for_seconds(-30, -30, 0.75)
    # dance floor

    motor_right.run_forever(speed_sp=-500)
    motor_left.run_forever(speed_sp=500)
    time.sleep(.5)

    while(True):
        motor_right.run_forever(speed_sp=-250)
        motor_left.run_forever(speed_sp=-250)
        time.sleep(.5)

        motor_right.run_forever(speed_sp=250)
        motor_left.run_forever(speed_sp=250)
        time.sleep(.5)


while True:
    if button.left:
        t1 = multiprocessing.Process(target=run1)
        t1.start()
        while not button.enter:
            time.sleep(0)
        t1.terminate()
        t1.join()
        stop()

    elif button.up:
        t2 = multiprocessing.Process(target=run2)
        t2.start()
        while not button.enter:
            time.sleep(0)
        t2.terminate()
        t2.join()
        stop()

    elif button.right:
        t3 = multiprocessing.Process(target=run3)
        t3.start()
        while not button.enter:
            time.sleep(0)
        t3.terminate()
        t3.join()
        stop()

    elif button.down:
        t4 = multiprocessing.Process(target=run4)
        t4.start()
        while not button.enter:
            time.sleep(0)
        t4.terminate()
        t4.join()
        stop()
