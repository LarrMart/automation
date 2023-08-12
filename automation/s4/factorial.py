#!/usr/bin/env python

import sys

def factorial(x):
  if(x == 0):
    return 1
  else:
    return x * factorial(x - 1)

value = sys.argv[1]

print(value + "! = " + str(factorial(int(value))))

