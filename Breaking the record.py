#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the breakingRecords function below.
def breakingRecords(scores):
    mn=scores[0]
    mx=scores[0]
    cmn=0
    cmx=0
    for score in scores:
        if(score>mx):
            mx=score
            cmx=cmx+1
        elif(score<mn):
            mn=score
            cmn=cmn+1
    
    
    return cmx,cmn

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
