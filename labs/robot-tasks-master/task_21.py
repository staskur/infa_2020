#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    n=1
    for j in range(13):

        move_down()
        move_right()
        for i in range(n):
            fill_cell()
            move_right()
        for i in range(n+1):
            move_left()
        n+=1
    move_down()
    move_right()

if __name__ == '__main__':
    run_tasks()
