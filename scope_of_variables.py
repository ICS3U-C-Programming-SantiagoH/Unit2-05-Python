#!/usr/bin/env python3
# Created By: Santiago Hewett
# Date: October 2, 2023
# This program shows how local and global variables work

# define the global variable
variable_x = 11


def local_variable():
    # this function shows what happens to local variables

    variable_x = 6
    variable_y = 3
    variable_z = variable_x + variable_y
    print(
        "Local variable_x, variable_y, variable_z, {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
        )
    )


def global_variable():
    # this function shows what happens to global variables

    global variable_x
    variable_y = 4
    variable_z = variable_x + variable_y
    print(
        "Global variable_x, variable_y, variable_z, {0} + {1} = {2}".format(
            variable_x, variable_y, variable_z
        )
    )


def main():
    # this function shows how local and global variables work

    local_variable()
    global_variable()


if __name__ == "__main__":
    main()
