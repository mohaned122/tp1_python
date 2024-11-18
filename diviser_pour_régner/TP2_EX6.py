while True:
    nb = int(input("donnez chiffre positive: "))
    if nb >= 0:
        break
    else:
        print("chiffre non positive")

for i in range(nb+1,nb+11,1):
    print(i)