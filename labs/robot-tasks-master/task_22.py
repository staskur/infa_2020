#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    def linia():
        n=0
        while not wall_is_on_the_right():
            fill_cell()
            move_right()
            n+=1
        else:
            fill_cell()
        if n!=0:
            move_left(n)

    while not wall_is_beneath():
        linia()
        move_down()
    else:
        linia()


if __name__ == '__main__':
    run_tasks()
