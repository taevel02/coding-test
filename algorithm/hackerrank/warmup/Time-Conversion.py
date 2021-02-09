#!/bin/python3

import os
import sys


#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    timestamp = s.split(':')

    if "PM" in timestamp[-1]:
        if timestamp[0] != '12':
            timestamp[0] = str(int(timestamp[0]) + 12)
        timestamp[-1] = timestamp[-1].replace("PM", "")

    if "AM" in timestamp[-1]:
        if timestamp[0] == '12':
            timestamp[0] = str(abs(int(timestamp[0]) - 12))
        if len(timestamp[0]) == 1:
            timestamp[0] = str(0) + timestamp[0]
        timestamp[-1] = timestamp[-1].replace("AM", "")

    return ':'.join(timestamp)


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
