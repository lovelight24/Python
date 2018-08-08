import os
import sys
#
# Complete the simpleArraySum function below.


def simple_array_sum(ar):
    ab = 0
    for x in ar:
        ab += x
    return ab


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    ar_count = int(input())
    ar = list(map(int, input().rstrip().split()))
    result = simple_array_sum(ar)
    fptr.write(str(result) + '\n')
    fptr.close()