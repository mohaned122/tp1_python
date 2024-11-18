print("donnez le moyenne")

while True:
    moy = int(input("moyenne: "))
    if (moy > 0 and moy < 20):
        break

if moy > 16:
    print("trés bien")
elif moy >=14:
    print("bien")
elif moy >= 12:
    print("assez bien")
elif moy >= 10:
    print("passable")



