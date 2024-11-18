
def multiplication(n):
    for i in range(1, n+1):
        for j in range(1, n+1):
            txt = "{:^2}"
            txt = txt.format(i*j)
            print(txt, end=" ")
        print()

x = int(input("Enter a number: "))
multiplication(x)