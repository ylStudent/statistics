"""
线性方程组求解
"""
import numpy as np
def guass(A: np.ndarray, b: np.ndarray):
    n = len(A)
    for j in range(n-1):
        for i in range(j+1, n):
            mult = A[i][j] / A[j][j]

            A[i,:] = A[i,:] - mult * A[j,:]
            # 可以改为：
            # A[i, j:] = A[i, j:] - mult * A[j, j:]

            b[i] = b[i] - mult * b[j]
    return A, b

def guass_lu(A):
    n = len(A)
    L = np.eye(n)
    
    for j in range(n-1):
        for i in range(j+1, n):
            mult = A[i][j] / A[j][j]

            A[i,j:] = A[i,j:] - mult * A[j,j:]

            L[i][j] = mult
    # return L, U
    return L, A


def lsolve(L, b):
    n = len(L)
    y = np.zeros(n)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])
    
    return y

def usolve(L, U, b):
    b = lsolve(L, b)

    n = len(b)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (b[i] - np.dot(U[i,:i:-1], x[:i:-1])) / U[i, i]
    return x

def solve(A, b):
    L, U = guass_lu(A)
    
    return usolve(L, U, b)

if __name__ == "__main__":
    A = np.array([[1, 2, 12], [4, 5, 6], [7, 8, 9]])
    b = np.array([9, 2, 14])
    x = solve(A.copy(), b.copy())
    
    if sum(np.matmul(A, x) == b):
        print("yes and x = ", x)
    else:
        print("no")
    
    print(np.linalg.solve(A, b))





