from karel.stanfordkarel import *

"""
File: CheckerboardKarel.py
Name: Michelle Lan
----------------------------
When you finish writing it, CheckerboardKarel should draw
a checkerboard using beepers, as described in Assignment 1. 
You should make sure that your program works for all of the 
sample worlds provided in the starter folder.
"""


def main():
    """
    Create a checkerboard pattern of beepers inside an empty rectangular world.
    """
    turn_left()
    # Karel is facing North.
    while front_is_clear():
        fill_two_line()
        # Two line as a set.
        go_to_next_set()
    fill_single_world()
    fill_single_street()


def go_to_next_set():
    if left_is_clear():
        turn_left()
        move()
        turn_left()


def fill_single_street():
    """
    If there is only one street in the world.
    """
    if facing_north():
        if not on_beeper():
            if not front_is_clear():
                turn_right()
                move()
                if not on_beeper():
                    turn_around()
                    # back to the initial position
                    move()
                    turn_around()
                    fill_one_line()


def turn_around():
    """
    turn left 2 times
    """
    for i in range(2):
        turn_left()


def fill_single_world():
    """
    If there is only (1,1) in the world.
    """
    if not front_is_clear():
        if not right_is_clear():
            if not left_is_clear():
                put_beeper()


def fill_two_line():
    """
    pre-condition: Karel is on the button of previous line, facing North.
    post-condition: Karel is at the top of next line, facing North.
    """
    fill_one_line()
    go_to_next_line()
    fill_one_line()


def fill_one_line():
    """
    pre-condition: Karel is on the button of the line, facing North.
    post-condition: Karel is at the top of the line, facing North.
    """
    if front_is_clear():
        put_beeper()
    while front_is_clear():
        move()
        if front_is_clear():
            move()
            put_beeper()


def go_to_next_line():
    """
    pre-condition: Karel is at the top of previous line, facing North.
    post-condition: Karel is on the button of next line, facing South.
    """
    turn_right()
    if front_is_clear():
        if on_beeper():
            move()
            turn_right()
            move()
        else:
            move()
            turn_right()


def turn_right():
    """
    turn left 3 times
    """
    for i in range(3):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)