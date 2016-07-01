import numpy as np
from math import *

def pi_n( n ):

     x = np.floor(22/7)
     dig = 1.0
     f_val = 22%7
     float(f_val)

     for i in range(n):
     
      dig = dig/10
      x = x + np.floor(f_val*10/7)*dig
      rem = (f_val*10)%7
      f_val =rem

     return x

print pi_n(5)

