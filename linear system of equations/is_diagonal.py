A = [[8, 3, -3], [-2, 1, 5], [3, 5, 10]] 

#A: coefficient of unknown variables
#X: initial guess for our method(Başlangıç Değer)
#Y: terms of the equations

def Is_DiagonalDominant(A: list[list[int]]) -> bool:
    """
    KKB matris yani 'kesin köşegen baskın' matris olup olmadığını kontrol ediyoruz. eğer kesin köşegensel matris ise True dönecek, değilse False.

    Keyword arguments:

    A: coefficient of unknown variable
    
    an instance;
    
    17$x_{1}$ + 5$x_{2}$ + 10$x_{3}$ = 15
    8$x_{1}$ + 15$x_{2}$ + 2$x_{3}$ = 12
    6$x_{1}$ + 2$x_{2}$ + 9$x_{3}$ = 7

    for those equations, A'll be

    A = [[17, 5, 10], [8, 15, 2], [6, 2, 9]]  
                       
    Return: True - False
    """
    
    length = len(A)
    diagonal = 0
    nondiagonal = 0

    for i in range(length):
        for j in range(length):
            if i == j:
                diagonal += abs(A[i][j])
            else:
                nondiagonal += abs(A[i][j])
    
    return True if diagonal > nondiagonal else False 

if __name__ == "__main__":
    if Is_DiagonalDominant(A) == True:
        print("Kesin Köşegen Baskın Matris")
    else:
        print("Kesin Köşegen Baskın Matris DEĞİL!")
