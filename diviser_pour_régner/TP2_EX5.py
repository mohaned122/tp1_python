#sexe
while True:
    gendre = input("donnez votre sexe M/F : ")
    if gendre == "M" or gendre == "m" or gendre == "F" or gendre == "f":
        break
    else:
        print("Vous ne pouvez pas choisir un sexe")

#taille
while True:
    taille = float(input("votre taille : "))
    if taille>0:
        break

#poids
while True:
    poids = float(input("votre poids : "))
    if poids>0:
        break

imc = (poids /(taille*taille))
print("votre imc = ",imc)

if gendre == "M" or gendre == "m":
    if imc >= 25:
        print(" vous devriez surveiller votre alimentation")
    elif imc <= 19:
        print("Vous devriez prendre des forces")
    else:
        print("Vous êtes à votre poids de forme")
elif gendre == "F" or gendre == "f":
    if imc >= 23:
        print(" vous devriez surveiller votre alimentation")
    elif imc <= 18:
        print("Vous devriez prendre des forces")
    else:
        print("Vous êtes à votre poids de forme")