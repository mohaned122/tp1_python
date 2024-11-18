while True:
    nb =int(input("Enter a number: "))
    if nb > 0:
        break

ok = True
for i in range(2,nb):
    if nb % i == 0:
        ok = False
        break


if ok:
 print("premier")
else:
    print("non premier")