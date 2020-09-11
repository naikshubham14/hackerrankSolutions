#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    fr={}
    for bird in arr:
        if(bird in fr):
            fr[bird]=fr[bird]+1
        else:
            fr[bird]=1

    mx = max(fr.values())

    almx = [k for k,v in fr.items() if v == mx]
    return min(almx)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
