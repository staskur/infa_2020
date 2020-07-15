#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
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

    move_down()
    for n in range(4):
        krest()
        move_right(4)
    else:
        krest()



if __name__ == '__main__':
    run_tasks()
