import math
import os
import random
import re
import sys

# Complete the diagonalDifference function below.
def diagonalDifference(arr):

if __name__ == '__main__':
    n = int(input())
    arr = []
    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))
    result = diagonalDifference(arr)
