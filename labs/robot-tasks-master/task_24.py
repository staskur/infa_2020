#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_1():
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
    move_right()
    krest()



if __name__ == '__main__':
    run_tasks()
