def jacobi(A, Y, x):
    """
    A: list[list[int]], Y: list[int], X: list[int]
    """
    length = len(A)
    jacob = x.copy() # direkt assignment yapınca aynı memory'de tutulduğundan tekrar Gauss-Seidel iterasyonu dönüyor.
    # yani jacob = X yapmak yerine jacob = X.copy() yapmalıyız.
    # jacob = X.copy() Shallow Copy denir. 
    # jacob = X yani direkt assignment'a ise Deep Copy denir.

    for i in range(length):
        sum_val = Y[i]
        for j in range(length):
                if (i != j):
                    sum_val -= A[i][j] * x[j]
        jacob[i] = sum_val / A[i][i]
    
    x = jacob.copy()

    return x


if __name__ == '__main__':
    A = [[8, 3, -3],[-2, -8, 5],[3, 5, 10]]
    Y = [14, 5, -8] 
    x = [0, 0, 0]   
    for i in range(5):
        x = jacobi(A, Y, x)
        print(x)