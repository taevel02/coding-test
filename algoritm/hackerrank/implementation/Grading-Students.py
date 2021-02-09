#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    final_grades = []
    for i in grades:
        nearst_grade = round((i+3)/5) * 5
        if nearst_grade < 40:
            final_grades.append(i)
        elif abs(nearst_grade - i) >= 3:
            final_grades.append(i)
        elif abs(nearst_grade - i) < 3:
            final_grades.append(nearst_grade)
    return final_grades


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
