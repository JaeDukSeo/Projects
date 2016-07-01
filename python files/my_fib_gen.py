import numpy as np
from math import *



def my_fib_gen(n):

   if (n==1)|(n==2):
      return 1

   else:
      return my_fib_gen(n-1)+ my_fib_gen(n-2)



print my_fib_gen(6)

 
