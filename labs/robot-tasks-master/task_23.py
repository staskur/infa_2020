#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    def linia():
        n=0
        while not wall_is_above():
            move_up()
            fill_cell()
            n+=1
        else:
            fill_cell()
        if n!=0:
            move_down(n)

    pos=0
    while not wall_is_on_the_right():
        if wall_is_beneath() and not wall_is_above():
            linia()
        move_right()
        pos+=1

    else:
        if wall_is_beneath() and not wall_is_above():
            linia()
        move_left(pos)


if __name__ == '__main__':
    run_tasks()
