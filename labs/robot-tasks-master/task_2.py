#!/usr/bin/python3

from pyrob.api import *

@task
def task_1_2():
    for n in range(3):
        move_down()
        move_right()
        if n==1 :
            fill_cell()
    move_right()

if __name__ == '__main__':
    run_tasks()
