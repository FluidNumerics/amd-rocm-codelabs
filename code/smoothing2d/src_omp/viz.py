#!/usr/bin/python3

import json
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

# Load the function and the smoothed function
f = np.loadtxt('function.txt')
smoothF = np.loadtxt('smooth-function.txt')

# Reshape the functions, assuming a square grid
nelem = len(f)
nx = int(np.sqrt(nelem))
f = f.reshape((nx,nx))
smoothF = smoothF.reshape((nx,nx))

# Create the figure, showing the original function in the upper plot
# and the smoothed function in the lower plot
fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols=1)
im = ax1.contourf(f,levels=np.arange(-1.0,1.0,0.1))
im = ax2.contourf(smoothF,levels=np.arange(-1.0,1.0,0.1))
plt.savefig("function.eps")


