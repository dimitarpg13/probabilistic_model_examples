# Cholesky Decomposition

The Cholesky decompositon of a Hermitian positive-definite matrix $A$, is a decomposition of the form:

$$A = LL^{*}$$

where $L$ is a lower triangular matrix with real and positive diagonal entries and $L^{*}$ denotes the conjugate transpose of $L$.

**Theorem**: Every Hermitian positive-definite matrix (and thus every real-valued symmetric positive-definite matrix) has a unique Cholesky decomposition.

The converse holds trivially - if $A$ can be written as $LL^{*}$ for some invertible $L$, lower-triangular or not, then $A$ is Hermitian and positive-definite.

For real matrix $A$ we write:

$$A = LL^{T}$$

where $L$ is a real lower triangular matrix with positive diagonal entries.

**Theorem**: Every Hermitian positive semidefinite matrix has Cholesky decomposition in the form $A = LL^{*}$ where the diagonal entries of $L$ are allowed to be zero. The decomposition is not unique in general. Additionally, if the rank of $A$ is $r$, then there is a unique lower triangular $L$ with exactly $r$ positive diagonal elements and $n-r$ columns containing all zeros. 

**Note**: the decomposition can be made unique when a pivoting choice is fixed. Formally:

**Theorem**: if $A$ is an $n \times n$ positive semidefinite matrix of rank $r$, then there is at least one permutation matrix $P$ such that $PAP^{T}$ has a unique decomposition of the form $PAP^{T} = LL^{*}$ with 
```math
L = \begin{bmatrix}L_1 & 0\\L_2 & 0\end{bmatrix}
```
where $L_1$ is an $r \times r$ lower triangular matrix with positive diagonal.

## Interpretation

The Cholesky decomposition is equivalent to a particular choice of conjugate axes of an ellipsoid. Let the ellipsoid be defined as $y^{T}Ay=1$, then by definition, a set of vectors $v_1,\dots,v_n$ are conjugate axes of the elippsoid $iff$ $v_{i}^{T}Av_j = {\delta}_{ij}$. 
