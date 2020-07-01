#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the decentNumber function below.
def decentNumber(n):
    if n<10 and n%3!=0 and n%5!=0 and (n-(n//5)*5)%3!=0:
        print(-1)
    else:
        l=0
        if n%3==0:
            print("5"*n)
        else:
            for i in range(n//5):
                z = (i+1)*5
                if (n-z)%3==0:
                    l = n-(i+1)*5
                    break
            print(l*"5"+(n-l)*"3")
    
        

if __name__ == '__main__':
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        decentNumber(n)
