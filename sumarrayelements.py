import math
import os
import random
import re
import sys

# Complete the aVeryBigSum function below.
def aVeryBigSum(ar):
    try:
        result = 0
        for x in range(0, len(ar)):
            result += ar[x]
        return result;
    except Exception as e:
        print(e)
if __name__ == '__main__':
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
    print(result)