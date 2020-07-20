#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
        def stolb():
            i=0
            while not wall_is_above():
                move_up()
                if not cell_is_filled():
                    fill_cell()
                else:
                    i+=1
            while not wall_is_beneath():
                move_down()
            return(i)

        n=0
        while not wall_is_on_the_right():
            if wall_is_above() and wall_is_beneath():
                fill_cell()
            if not wall_is_above():
                n+=stolb()
            move_right()
        mov("ax",n)


if __name__ == '__main__':
    run_tasks()
