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
Then the ellipsoid is given by:
```math
\biggl\{\sum_{i}{x_i}{v_i}:{x^T}{x}=1\biggr\}=f\left({\mathbb{S}}^{n}\right)
```
where $f$ maps the basis vector $e_i \mapsto v_i$ and ${\mathbb{S}}^{n}$ is the unit sphere in $n$ dimensions. That is, the ellipsoid is a linear image of the unit sphere.

Define the matrix $V := \[v_1|v_2|\dots|v_n\]$, then ${v_i}^{T}Av_j = {\delta}_{ij}$ is equivalent to $V^{T}AV = I$. Different choices of the conjugate axes correspond to different decompositions.

The Cholesky decomposition corresponds to choosing $v_1$ to be parallel to the first axis, $v_2$ to be within the plane spanned by the first two axes, and so on.
This makes $V$ an upper-triangular matrix because $v\_k = {\alpha}_{1} {v\_1} + {\alpha}\_{2} {v\_2} + \dots + {\alpha}\_{k-1} {v\_{k-1}}$ where ${\alpha}\_l, l=1,\dots,k-1$ are real numbers not all equal to zero. Since the inverse of upper triangular matrix is also upper triangular matrix and the transpose of the inverse is lower triangular we have: $A = LL^{T}$ where $L = {\left(V^{-1}\right)}^{T}$ is lower triangular. 

In [Singular Value Decomposition](https://github.com/dimitarpg13/probabilistic_model_examples/blob/main/docs/SingularValueDecomposition.md) we choose $v_1,\dots,v_n$ to be perpendicular. Then, let $\lambda = \frac{1}{{\lVert v_i \rVert}^2}$ and $\Sigma = \text{diag}\left({\lambda}_1,\dots,\lambda_n\right)$ and there is $V = U{\Sigma}^{-1/2}$ where $U$ is an orthogonal matrix. This then yields $A = U{\Sigma}{U}^{T}$. 
