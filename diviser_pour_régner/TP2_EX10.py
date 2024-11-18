a = 4
b = 5
mult = 0

if a < b :
    a,b = b,a

for i in range(a):
    mult += b

print(mult)