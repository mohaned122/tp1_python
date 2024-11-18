def tri_fusion(liste):
    # Si la liste ne contient qu'un élément ou est vide, elle est déjà triée
    if len(liste) <= 1:
        return liste

    # On divise la liste en deux moitiés
    print("diviser\n")
    milieu = len(liste) // 2
    gauche = liste[:milieu]
    droite = liste[milieu:]
    print("gauche", gauche)
    print("droite", droite)
    
    # On applique récursivement le tri fusion sur les deux moitiés
    gauche_triee = tri_fusion(gauche)
    droite_triee = tri_fusion(droite)

    # On fusionne les deux moitiés triées
    print("\n ************************régner******************************")
    print("gauche_tri", gauche_triee)
    print("droite_tri", droite_triee)
    return fusion(gauche_triee, droite_triee)


def fusion(gauche, droite):
    resultat = []
    i, j = 0, 0

    # On compare les éléments de gauche et de droite et on les ajoute au résultat dans l'ordre croissant
    while i < len(gauche) and j < len(droite):
        if gauche[i] < droite[j]:
            resultat.append(gauche[i])
            i += 1
        else:
            resultat.append(droite[j])
            j += 1

    # On ajoute les éléments restants de gauche ou de droite
    resultat.extend(gauche[i:])
    resultat.extend(droite[j:])

    return resultat


# Exemple d'utilisation
liste = [38, 27, 43, 3, 9, 82, 10]
liste_triee = tri_fusion(liste)
print("\n ***************************************** \n")
print("Liste triée:", liste_triee)
