import is_diagonal
import gauss_seidel
import jacobi

A = [[8, 3, -3], [-2, -8, 5], [3, 5, 10]] 
Y = [14, 5, -8] 
X = [0, 0, 0]
x = [0, 0, 0] 

for i in range(5):
    if is_diagonal.Is_DiagonalDominant(A):
        X = gauss_seidel.gauss_seidel(A, Y, X)
        x = jacobi.jacobi(A, Y, x)
        print(X)
        print(x)