def factoriel(n,rst):
    if n == 1:
        print(rst)
        print(n)
    else:
         factoriel(n-1, rst*n)
         print(n)


factoriel(5,1)