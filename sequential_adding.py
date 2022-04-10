#!/usr/bin/env python3

# Created by Aidan Lalonde-Novales
# Created April 2022
# This program tells a user the sum of the sequential
# numbers preceding that of what they entered.


def main():
    # this function determines sequential sum
    counter = 0
    sum_count = 0

    # input
    times_to_loop_string = input("Please enter a positive integer: ")

    # process & output
    try:
        times_to_loop = int(times_to_loop_string)

        while counter <= times_to_loop:
            sum_count = sum_count + counter
            counter = counter + 1
        print(
            "The sum of all sequential numbers preceding {0} is {1}.".format(
                times_to_loop, sum_count
            )
        )

    except Exception:
        print("Your integer is invalid! Please try again.")

    print("\nDone.")


if __name__ == "__main__":
    main()
