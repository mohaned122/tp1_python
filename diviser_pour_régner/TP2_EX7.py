a = 27
b = 9

while True:
    if a > b :
        a = a-b
    elif b > a:
        b = b-a
    elif a == b or a<0 or b<0:
        break

print(a)