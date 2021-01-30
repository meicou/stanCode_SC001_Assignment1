from karel.stanfordkarel import *

"""
File: StoneMasonKarel.py
Name: Michelle Lan
--------------------------------
At present, the StoneMasonKarel file does nothing.
Your job in the assignment is to add the necessary code to
instruct Karel to build a column (a vertical structure
that is 5 beepers tall) in each avenue that is either on the right
or left side of the arch, as described in the Assignment 1 handout. 
Karel should end on the last avenue, 1st Street, facing east. 
"""


def main():
    """
    Karel repairs some set of arches where some of the stones are missing from the columns supporting the arches.
    """
    put_beeper()
    while front_is_clear():
        repair_column()
        down()
        move_to_next_column()
    repair_column()
    down()


def repair_column():
    """
    pre-condition: Karel is on the button of the column, facing North.
    post-condition: Karel is on the top of the column, facing South.
    """
    turn_left()
    # Karel is facing North.
    while front_is_clear():
        move()
        if not on_beeper():
            put_beeper()
    turn_around()
    # Karel is facing South.


def turn_around():
    """
    turn left 2 times
    """
    for i in range(2):
        turn_left()


def down():
    """
    pre-condition: Karel is on the top of the column, facing South.
    post-condition: Karel is on the button of the column, facing East.
    """
    while front_is_clear():
        move()
        if not on_beeper():
            put_beeper()
    turn_left()
    # Karel is facing East.


def move_to_next_column():
    """
    pre-condition: Karel is on the button of the previous column, facing East.
    post-condition: Karel is on the button of the next column, facing East.
    """
    for i in range(4):
        move()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    execute_karel_task(main)
