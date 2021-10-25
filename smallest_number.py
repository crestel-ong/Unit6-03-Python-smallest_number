#!/usr/bin/env python3

# Created by: Crestel Ong
# Created on: Oct 2021
# this is the max number program in python
# finds the smallest number out of 10 randomly generated numbers and prints it
# this program uses arrays as parameter

import random


def smallest_number(random_number_list):
    # this function finds the smallest number in the list
    # finds the min number

    small_number = random_number_list[1]

    for loop_counter in random_number_list:
        # its called loopcounter but thats just the name
        # this 'loop_counter' is holding some random gen #
        if loop_counter < small_number:
            small_number = loop_counter

    return small_number


def main():
    # this function uses a list
    # this function gets and generates random numbers

    random_number_list = []
    # loop_counter = 0

    print("Here is a list of 10 randomly generated numbers:")
    print(" ")
    for loop_counter in range(10):
        single_number = random.randint(1, 100)
        random_number_list.append(single_number)
        print("Random number {0} is : {1}".format(loop_counter + 1, single_number))

    # call function
    min_number = smallest_number(random_number_list)

    # output
    print("\nThe smallest number is {0}.".format(min_number))
    print("\nDone.")


if __name__ == "__main__":
    main()
