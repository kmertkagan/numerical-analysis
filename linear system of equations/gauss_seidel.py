def gauss_seidel(A: list[list[int]], Y: list[int], X: list[int]):
    """
    A = [[5, 2, -1], [7, -15, 4], [-2, -8, -11]] Lineer Denklem Sistemimizdeki Denklem Elemeanlarının Katsayıları\n
    Y = [15, 8, 7] Sonuçlar\n
    X = [0, 0, 0] Başlangıç Değer\n
    olsun.
    
    Burada işlemler sırasıyla;
    1- A matrisinde 1 listeyi tuttuk ve Y matrisindeki aynı sıradaki elemanı tutuyoruz.(dongu1) ornek --> [5, 2, -1], 15 ya da [7, -15, 4], 8 gibi\n
    2- sonrasında Y matrisinde tuttuğumuz değeri(15 ya da 8), A matrisindeki tutmadığımız değerleri ve X matrisindeki değerlerin çarpımından çıkartıyoruz.(dongu2)(Koda Bakabilirsiniz, anlatım karışık oldu)\n
    3- tüm bunlar bittikten sonra 2. aşamadaki çıkan değeri, 1. aşamadaki A matrisinden çıkan listedeki indexe denk düşen elemana bölüyoruz.(dongu1) ornek --> [5, 2, -1] 1.index için 5, [7, -15, 4] 2.index için -15 gibi\n 
    4- son 3.aşamadaki çıkan değerler hepsini eşitliyoruz X(başlangıç değer)'e eşitliyoruz ve döngü bittikten sonra return olarak X(başlangıç değer) dönüyoruz. X = [0, 0, 0]
    """

    n = len(A) # to find no of rows or col of sq matrix A
    for i in range(n):
        sum_val = Y[i]
        for j in range(n):
            if (i != j):
                sum_val -= A[i][j] * X[j]
        X[i] = sum_val / A[i][i]
    return X




if __name__ == '__main__':
    A = [[8, 3, -3],[-2, -8, 5],[3, 5, 10]] #coefficient of unknown variables
    Y = [14, 5, -8] #terms that appears after '=' sign in the equation
    X = [0, 0, 0]   
    X = gauss_seidel(A, Y, X)
    print(X)