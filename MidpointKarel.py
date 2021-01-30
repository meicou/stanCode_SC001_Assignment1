from karel.stanfordkarel import *

"""
File: MidpointKarel.py
Name: Michelle Lan
----------------------------
When you finish writing it, MidpointKarel should
leave a beeper on the corner closest to the center of 1st Street
(or either of the two central corners if 1st Street has an even
number of corners).  Karel can put down additional beepers as it
looks for the midpoint, but must pick them up again before it
stops.  The world may be of any size, but you are allowed to
assume that it is at least as tall as it is wide.
"""


def main():
    """
    Karel places a single beeper at the midpoint of 1st street and end up at midpoint.
    """
    put_beeper()
    if front_is_clear():
        calculate_avenue()
        half()
        go_midpoint()
        back_to_midpoint()


def calculate_avenue():
    """
    pre-condition: Karel is at (1,1), facing East.
    post-condition: Karel is at the end of 1st street, facing East.
    """
    while front_is_clear():
        move()
        put_beeper()
        turn_around()
        pick_previous_beeper()


def pick_previous_beeper():
    """
    pre-condition: Karel is at the next position, facing West.
    post-condition: Karel is at the same position, facing East.
    """
    move()
    while on_beeper():
        pick_beeper()
        turn_around()
        move()
        put_beeper()
        turn_around()
        move()
    if not on_beeper():
        turn_around()
        move()


def turn_around():
    """
    turn left 2 times
    """
    for i in range(2):
        turn_left()


def half():
    """
    pre-condition: Karel is on the last avenue, facing West.
    post-condition: Karel is on the last avenue, facing West.
    """
    turn_around()
    # Karel is facing West.
    while on_beeper():
        pick_two_put_one()


def pick_two_put_one():
    """
    pre-condition: Karel is on the last avenue, facing West.
    post-condition: Karel is on the last avenue, facing West.
    """
    pick_beeper()
    if on_beeper():
        pick_beeper()
        move()
        while on_beeper():
            move()
        if not on_beeper():
            put_beeper()
            move_back()


def move_back():
    """
    pre-condition: Karel is facing West.
    post-condition: Karel is on the last avenue, facing West.
    """
    turn_around()
    # Karel is facing East.
    while front_is_clear():
        move()
    turn_around()


def go_midpoint():
    """
    pre-condition: Karel is on the last avenue, facing West.
    post-condition: Karel is next to the midpoint, facing West.
    """
    move()
    while on_beeper():
        if front_is_clear():
            pick_beeper()
            move()
        else:
            pass


def back_to_midpoint():
    """
    pre-condition: Karel is next to the midpoint, facing West.
    post-condition: Karel is on the midpoint, facing East.
    """
    if front_is_clear():
        turn_around()
        move()
        put_beeper()


# DO NOT EDIT CODE BELOW THIS LINE #


if __name__ == '__main__':
    execute_karel_task(main)
