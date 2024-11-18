
"""
def permutation(a,b):
    txt = "a : {:^2} , b : {:^2}"
    print("before permutation " + txt.format(a,b))
    a +=b
    b = a-b
    a= a-b
    print("after permutation " + txt.format(a,b))

permutation(7,9)
"""
a = 10
b = 13
txt = "a : {:^2} , b : {:^2}"
print("before permutation " + txt.format(a,b))
a,b = b,a
print("after permutation " + txt.format(a,b))