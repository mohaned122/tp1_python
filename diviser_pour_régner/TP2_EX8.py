a = 10
b = 100
c = 70


if a+b >= c:
    print("les longueurs correspondent à un triangle")
    if a ** 2 + b ** 2 == c ** 2 and a == b:
        print("le triangle est isocèle et rectangle")
    elif a == b == c:
        print("le triangle est équilatérale")
    elif a ** 2 + b ** 2 == c ** 2:
        print(" le triangle est rectangle")
else:
    print("c'est n'st pas un rectangle")
