
def pair(n):
    if n == 0:
        return "nombre pair"
    else:
        impair(n-1)

def impair(n):
    if n == 1:
        return "nombre impair"
    else:
        pair(n-1)

n = int(input("donnez une entier: "))
print(pair(n))

"""
n = int(input("donnez une entier: "))
print("le nb : ",n ," est paire : ",n%2 == 0)
"""

