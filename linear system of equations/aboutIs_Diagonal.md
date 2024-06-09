KKB matris yani 'kesin köşegen baskın' matris olup olmadığını kontrol ediyoruz. eğer kesin köşegensel matris ise True dönecek, değilse False.

## Teorem;
$i = 1, 2, \dotsb, n$
olsun

$$|a_{ij}| >  \sum_{i = 1 ,\ j \neq i}^{n} |a_{ij}|$$
eşitsizliği sağlanır ise bu ifade *Kesin Köşegen Baskın Matristir.*

**Açıklama için;**

*Lineer Denklem Sistemimizi aşağıdaki gibi düşünelim.*
$$
\left(\begin{matrix} 
x_{11} & x_{12} & \cdots & x_{1n}\\
x_{21} & x_{22} & \cdots & x_{2n}\\
\vdots & \vdots & \ddots & \vdots\\                    
x_{n1} & x_{n2} & \cdots & x_{nn}
\end{matrix}\right)  
$$

*Köşegen Matrislerimiz aşağıdaki gibidir:*

$x_{11}, x_{22}, \dots, x_{nn}$

bu köşe matrislerin mutlak değeri, kendi satırlarında bulunan diğer indekslerin mutlak değerlerinin toplamından büyük ise ve bu tüm köşe matrisleri için geçerli ise bu matris *Kesin Köşegen Baskın* Matris olur.


**örnek olarak lineer denklemimiz aşağıdaki gibi olsun:**
    
17$x_{1}$ + 5$x_{2}$ + 10$x_{3}$ = 15\
8$x_{1}$ + 15$x_{2}$ + 2$x_{3}$ = 12\
6$x_{1}$ + 2$x_{2}$ + 9$x_{3}$ = 7

buna göre matris
$$\ A =
\left(\begin{matrix} 
17 & 5 & -10\\\\
8 & -15 & 2\\\\
6 & -2 & 9
\end{matrix}\right)  
$$

şeklinde olur. az önceki anlatılanı uygularsak:

$|17| > |5| + |-10|$ ve

$|-15| > |8| + |2|$ ve 

$|9| > |6| + |-22|$ 


doğru olduklarına göre bu matrisimiz Kesin Köşegen Baskın matristir.





