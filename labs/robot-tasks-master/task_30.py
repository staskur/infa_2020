#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    n = 0
    while not wall_is_on_the_right():
       n += 1
       move_right()
    move_left(n)

    for i in range(n+1):
        for j in range(n+1):
            if i!=j and i!=n-j:
                fill_cell()
            if j!=n:
                move_right()
        move_left(n)
        if i!=n:
            move_down()


if __name__ == '__main__':
    run_tasks()
