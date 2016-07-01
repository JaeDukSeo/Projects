import numpy as np
from math import *


def e_n (n):
   x = np.floor(np.exp(1))
   dig = 1.0;
   f_val = np.exp(1)-x;
   
   print x,f_val 
   for i in range(n):
       f_val =f_val*10
       dig = dig/10;
       x = x+ np.floor(f_val)*dig;
       print x, f_val,dig
       f_val = f_val - np.floor(f_val);       
       

   return x

print e_n(4)

