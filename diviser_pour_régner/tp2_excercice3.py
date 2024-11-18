pu = int(input("prix unitaire de l'heur: "))
heur_total = int(input("donnez le nombre de heur :"))
salaire_initiale = 39 * pu
sup_sal = 0
sup = heur_total - 39

while True:
    """if sup <= 0:
        break
    elif (heur_total > 39) and (heur_total <= 44):
        sup_sal = sup * 1.5 * pu
        sup = heur_total - 44
    elif (heur_total > 44) and (heur_total <= 49):
        sup_sal = sup * 1.75 * pu
        sup = heur_total - 49
    el"""
    if heur_total > 49:
        sup_sal = sup * 2 * pu
        sup = 0
    elif heur_total > 44:
        sup_sal = sup * 1.75 * pu
        sup = heur_total - 49


    print(sup)

salaire = salaire_initiale + sup_sal
print("sailaire :",salaire)





