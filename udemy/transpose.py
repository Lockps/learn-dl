import numpy as np
import torch

enter = "\n\n"
# create a vector
nv = np.array([[1,2,3,4]])
print(nv,end=enter)

# Transpose
print(nv.T , end=enter)

# Transpose and Transpose
print(nv.T.T , end=enter)

