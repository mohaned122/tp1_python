while True:
    nb =int(input("Enter a number: "))
    if nb > 0:
        break

som=0
for i in range(1,nb//2+1):
    if nb % i == 0:
        som +=i

if som == nb:
    print("parfait")
else:
    print("non parfait")