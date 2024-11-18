time = input("Enter a time: ")
tabTime = time.split(":")
heur = int(tabTime[0])
min = int(tabTime[1])
sec = int(tabTime[2])
sec =sec + 1
if sec == 60:
    min = min +1
    sec = 0
    if min == 60:
        heur = heur +1
        if heur == 24:
            heur = 0
            min = 0
            sec = 0

txt = "{}:{}:{}".format(heur, min, sec)
print(txt)