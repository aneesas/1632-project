import numpy as np


def inv_2x2(A):
    """Returns inverse of 2x2 matrix A"""
    assert A.shape == (2, 2), "Wrong shape for matrix A, cannot invert"

    a11 = A[0,0]
    a12 = A[0, 1]
    a21 = A[1, 0]
    a22 = A[1,1]

    det = a22 * a11 - a12 * a21
    assert det != 0, "Singular matrix!"
    return np.array([[a22/det, -a12/det],
                     [-a21/det, a11/det]])

# Math from https://semath.info/src/inverse-cofactor-ex4.html
def inv_4x4(A):
    """Returns inverse of 4x4 matrix A"""
    assert A.shape == (4,4), "Wrong shape for matrix A, cannot invert"

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

    # Determinant
    det = a11*a22*a33*a44 + a11*a23*a34*a42 + a11*a24*a32*a43 \
        - a11*a24*a33*a42 - a11*a23*a32*a44 - a11*a22*a34*a43 \
        - a12*a21*a33*a44 - a13*a21*a34*a42 - a14*a21*a32*a43 \
        + a14*a21*a33*a42 + a13*a21*a32*a44 + a12*a21*a34*a43 \
        + a12*a23*a31*a44 + a13*a24*a31*a42 + a14*a22*a31*a43 \
        - a14*a23*a31*a42 - a13*a22*a31*a44 - a12*a24*a31*a43 \
        - a12*a23*a34*a41 - a13*a24*a32*a41 - a14*a22*a33*a41 \
        + a14*a23*a32*a41 + a13*a22*a34*a41 + a12*a24*a33*a41
    assert det != 0, "Singular matrix!"

    # Adjugate matrix
    A11 = a22*a33*a44 + a23*a34*a42 + a24*a32*a43 - a24*a33*a42 - a23*a32*a44 - a22*a34*a43
    A12 = -a12*a33*a44 - a13*a34*a42 - a14*a32*a43 + a14*a33*a42 + a13*a32*a44 + a12*a34*a43
    A13 = a12*a23*a44 + a13*a24*a42 + a14*a22*a43 - a14*a23*a42 - a13*a22*a44 - a12*a24*a43
    A14 = -a12*a23*a34 - a13*a24*a32 - a14*a22*a33 + a14*a23*a32 + a13*a22*a34 + a12*a24*a33
    A21 = -a21*a33*a44 - a23*a34*a41 - a24*a31*a43 + a24*a33*a41 + a23*a31*a44 + a21*a34*a43
    A22 = a11*a33*a44 + a13*a34*a41 + a14*a31*a43 - a14*a33*a41 - a13*a31*a44 - a11*a34*a43
    A23 = -a11*a23*a44 - a13*a24*a41 - a14*a21*a43 + a14*a23*a41 + a13*a21*a44 + a11*a24*a43
    A24 = a11*a23*a34 + a13*a24*a31 + a14*a21*a33 - a14*a23*a31 - a13*a21*a34 - a11*a24*a33
    A31 = a21*a32*a44 + a22*a34*a41 + a24*a31*a42 - a24*a32*a41 - a22*a31*a44 - a21*a34*a42
    A32 = -a11*a32*a44 - a12*a34*a41 - a14*a31*a42 + a14*a32*a41 + a12*a31*a44 + a11*a34*a42
    A33 = a11*a22*a44 + a12*a24*a41 + a14*a21*a42 - a14*a22*a41 - a12*a21*a44 - a11*a24*a42
    A34 = -a11*a22*a34 - a12*a24*a31 - a14*a21*a32 + a14*a22*a31 + a12*a21*a34 + a11*a24*a32
    A41 = -a21*a32*a43 - a22*a33*a41 - a23*a31*a42 + a23*a32*a41 + a22*a31*a43 + a21*a33*a42
    A42 = a11*a32*a43 + a12*a33*a41 + a13*a31*a42 - a13*a32*a41 - a12*a31*a43 - a11*a33*a42
    A43 = -a11*a22*a43 - a12*a23*a41 - a13*a21*a42 + a13*a22*a41 + a12*a21*a43 + a11*a23*a42
    A44 = a11*a22*a33 + a12*a23*a31 + a13*a21*a32 - a13*a22*a31 - a12*a21*a33 - a11*a23*a32

    # Divide all the elements by determinant, which we have to do individually because YAPSS
    # doesn't support multiplying a numpy array by a float
    A11 = A11 / det
    A12 = A12 / det
    A13 = A13 / det
    A14 = A14 / det
    A21 = A21 / det
    A22 = A22 / det
    A23 = A23 / det
    A24 = A24 / det
    A31 = A31 / det
    A32 = A32 / det
    A33 = A33 / det
    A34 = A34 / det
    A41 = A41 / det
    A42 = A42 / det
    A43 = A43 / det
    A44 = A44 / det

    A_inv = np.array([[A11, A12, A13, A14],
                      [A21, A22, A23, A24],
                      [A31, A32, A33, A34],
                      [A41, A42, A43, A44]])
    return A_inv


if __name__ == "__main__":
    print("Testing inv_4x4...")

    A = np.array([[1, 1, 1, -1],
                  [1, 1, -1, 1],
                  [1, -1, 1, 1],
                  [-1, 1, 1, 1]])
    
    assert np.allclose(np.linalg.inv(A), inv_4x4(A)), "Matrix {} failed".format(A)

    A = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 0, 11, 12],
                  [13, 14, 15, 6]])

    assert np.allclose(np.linalg.inv(A), inv_4x4(A)), "Matrix {} failed".format(A)

    A = np.array([[0, -1, -2, 4],
                  [-6, 7, 1, 3],
                  [0.5, 8, -8, 9],
                  [-0.5, -7, 2, -4]])

    assert np.allclose(np.linalg.inv(A), inv_4x4(A)), "Matrix {} failed".format(A)

    print("Tests passed.")