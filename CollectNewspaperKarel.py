from karel.stanfordkarel import *

"""
File: CollectNewspaperKarel.py
Name: Michelle Lan
--------------------------------
At present, the CollectNewspaperKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to walk to the door of its house, pick up the
newspaper (represented by a beeper, of course), and then return
to its initial position in the upper left corner of the house.
"""


def main():
    """
    Karel picks up the newspaper located outside the doorway and then returns to its initial position.
    """
    move_to_newspaper()
    pick_beeper()
    bring_back_newspaper()
    put_beeper()


def move_to_newspaper():
    """
    pre-condition: Karel is in the northwest corner of its house, facing East.
    post-condition: Karel is on the newspaper located outside the doorway, facing West.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_left()
    move()
    turn_around()
    # Karel is facing West.


def bring_back_newspaper():
    """
    pre-condition: Karel is outside the doorway, facing West.
    post-condition: Karel is in the northwest corner of its house, facing East.
    """
    while front_is_clear():
        move()
    turn_right()
    move()
    turn_right()


def turn_right():
    """
    turn left 3 times
    """
    for i in range(3):
        turn_left()


def turn_around():
    """
    turn left 2 times
    """
    for i in range(2):
        turn_left()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
