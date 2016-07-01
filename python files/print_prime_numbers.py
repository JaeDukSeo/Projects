import numpy as np
from math import *


def det_prime(n):

    sq_root = np.floor(sqrt(n));
    count = 0;

    for i in range(2,int(sq_root)+1):

       if n%i == 0:
          count = count+1

    if(count>0):
        return 1
    else:
        return 0



