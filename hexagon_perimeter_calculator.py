#!/usr/bin/env python3

# Created by Marwan Mashaly
# Created on September 2019
# This program calculates the perimeter of a hexagon
#    with user input


def main():
    # this function calculates perimeter of a hexagon

    # input
    sidelength = int(input("Enter sidelength of the rectangle (cm): "))

    # process
    perimeter = 6*sidelength

    # output
    print("")
    print("Perimeter is {}cm ".format(perimeter))


if __name__ == "__main__":
    main()
