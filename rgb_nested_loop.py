#!/usr/bin/env python3
# Created By: Noah Ouellette
# Date: Jan. 14, 2022
# This program prints out all of the possible RGB
# values up to 50 for each colour

import colorama
import random
import time
from colorama import Fore, Back, Style


def main():

    # Initialize the three counters
    counter1 = 0
    counter2 = 0
    counter3 = 0

    # Print intro message
    print("Here are all of the RGB values up to 50")

    # Loop that counts the Red number
    for counter3 in range(51):

        # Loop that counts the Green number
        for counter2 in range(51):

            # Loop that counts the Blue number
            for counter1 in range(51):
                print("RGB {}, {}, {}".format(counter3, counter2, counter1))


if __name__ == "__main__":
    main()
