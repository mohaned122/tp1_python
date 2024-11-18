def div_euclidien(a,b):
    return b//a, b%a

a = int(input("Enter 'a' number: "))
b = int(input("Enter 'b' number: "))

print(b,"=",a,"*",div_euclidien(a,b)[0],"+",div_euclidien(a,b)[1])