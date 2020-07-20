#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_30():
    dyr=1
    while dyr==1:
        dyr=0
        while wall_is_beneath() and not wall_is_on_the_left():
            move_left()
        if not wall_is_beneath():
            move_down()
            dyr=1
            while not wall_is_on_the_right():
                move_right()


if __name__ == '__main__':
    run_tasks()
