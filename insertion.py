#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
# 
def insertionSort1(n, arr):
    val = arr[-1]
    # Write your code here
    for i in range(n-2,-1,-1):
        if val < arr[i]:
            arr[i+1]=arr[i]
        else:
            arr[i+1]=val
            break
        print(*arr,end=' ')  
        print()
        
        if i == 0:
            arr[i] = val
            
    print(*arr,end=' ')  
  
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
