from __future__ import division
import numpy as np
import matplotlib.pyplot as pl

def kernel(a, b):
    """Gaussian Process squared exponential kernel"""
    sqdist = np.sum(a**2,1).reshape(-1,1) + np.sum(b**2,1) - 2*np.dot(a, b.T)
    return np.exp(-0.5*sqdist)


