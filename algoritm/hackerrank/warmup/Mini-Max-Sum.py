#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    minimum_sum, maximum_sum = 0, 0

    arr.sort()
    for i in range(4):
        minimum_sum += arr[i]
        maximum_sum += arr[len(arr) - 1 - i]

    print(minimum_sum, maximum_sum)


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
