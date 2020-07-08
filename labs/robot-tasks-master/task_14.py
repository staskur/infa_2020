#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():

    def  fillcell():
        if wall_is_beneath() and wall_is_above():
            fill_cell()
        if not wall_is_beneath():
            move_down()
            fill_cell()
            move_up()
        if not wall_is_above():
            move_up()
            fill_cell()
            move_down()

    while not wall_is_on_the_right():
        fillcell()
        move_right()
    else:
        fillcell()

if __name__ == '__main__':
    run_tasks()
