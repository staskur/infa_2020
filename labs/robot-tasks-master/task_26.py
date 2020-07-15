#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    def krest():
        move_down()
        fill_cell()
        move_right()
        fill_cell()
        move_right()
        fill_cell()
        move_left()
        move_down()
        fill_cell()
        move_up(2)
        fill_cell()
        move_left()

    for s in range(4):
        for n in range(9):
            krest()
            move_right(4)
        else:
            krest()
            move_left(36)
        move_down(4)
    else:
        for n in range(9):
            krest()
            move_right(4)
        else:
            krest()
            move_left(36)


if __name__ == '__main__':
    run_tasks()
