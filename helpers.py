import numpy as np

def inv_4x4(A):
    """Returns inverse of 4x4 matrix A"""
    assert A.shape == (4,4), "Wrong shape for matrix A, cannot invert"

    det = np.det(A)
    assert det != 0, "Singular matrix!"

    # Original matrix elements
    a11 = A[0, 0]
    a12 = A[0, 1]
    a13 = A[0, 2]
    a14 = A[0, 3]
    a21 = A[1, 0]
    a22 = A[1, 1]
    a23 = A[1, 2]
    a24 = A[1, 3]
    a31 = A[2, 0]
    a32 = A[2, 1]
    a33 = A[2, 2]
    a34 = A[2, 3]
    a41 = A[3, 0]
    a42 = A[3, 1]
    a43 = A[3, 2]
    a44 = A[3, 3]

    # Adjugate matrix
    A11 = a22*a33*a44 + a23*a34*a42 + a24*a32*a43 - a24*a33*a42 - a23*a32*a44 - a22*a34*a43
    A12 = -a12*a33*a44 - a12*a32*a44 - a22*a34*a43 + a14*a33*a42 + a13*a32*a44 + a12*a34*a43
    A13 = a12*a23*a44 + a13*a24*a42
    A14 = 0.
    A21 = 0.
    A22 = 0.
    A23 = 0.
    A24 = 0.
    A31 = 0.
    A32 = 0.
    A33 = 0.
    A34 = 0.
    A41 = 0.
    A42 = 0.
    A43 = 0.
    A44 = 0.

    A_inv = 1./det * np.array([[A11, A12, A13, A14],
                               [A21, A22, A23, A24],
                               [A31, A32, A33, A34],
                               [A41, A42, A43, A44]])
    return A_inv

# TODO might not need this
def matmul_4d(A, x):
    """Implements A @ x for A dim (4,4) and x dim (4,1)"""
    assert A.shape == (4,4), "Wrong shape for matrix A, cannot multiply"
    assert x.shape == (4,1) or x.shape == (4,), "Wrong shape for vector x, cannot multiply"

    b = np.zeros((4, 1))
    b[0] = A[0, 0] * x[0] + A[0, 1] * x[1] + A[0, 2] * x[2] + A[0, 3] * x[3]
    b[1] = A[1, 0] * x[0] + A[1, 1] * x[1] + A[1, 2] * x[2] + A[1, 3] * x[3]
    b[2] = A[2, 0] * x[0] + A[2, 1] * x[1] + A[2, 2] * x[2] + A[2, 3] * x[3]
    b[3] = A[3, 0] * x[0] + A[3, 1] * x[1] + A[3, 2] * x[2] + A[3, 3] * x[3]

    return b