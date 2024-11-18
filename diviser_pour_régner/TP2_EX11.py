while True:
    nb =int(input("Enter a number: "))
    if nb > 0:
        break

som = 1
while nb >= 1:
    som *= nb
    nb -= 1

print("factoriel : ",som)