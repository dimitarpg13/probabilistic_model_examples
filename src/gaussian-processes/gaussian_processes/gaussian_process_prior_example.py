from __future__ import division
import numpy as np
import matplotlib.pyplot as pl


def kernel(a, b):
    """Gaussian Process squared exponential kernel"""
    sq_dist = np.sum(a**2,1).reshape(-1,1) + np.sum(b**2,1) - 2*np.dot(a, b.T)
    return np.exp(-0.5*sq_dist)


n = 100 # number of test points
epsilon = 1e-06 # sufficiently small number
xtest = np.linspace(-5, 5, n).reshape(-1, 1)  # test points
kernel = kernel(xtest, xtest)  # kernel at test points

# draw samples from the prior at our test points
L = np.linalg.cholesky(kernel + epsilon*np.eye(n))
f_prior = np.dot(L, np.random.normal(size=(n,10)))

pl.plot(xtest, f_prior)
pl.show()
