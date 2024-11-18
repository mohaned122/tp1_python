MAX = int(input("Entrez la valeur maximale: "))

somme = 0
produit = 1
somme_inverses = 0

for i in range(1, MAX + 1):
    if i % 5 != 0:
        somme += i
        produit *= i
        somme_inverses += 1 / i


print("Somme:", somme)
print("Produit:", produit)
print("Somme des inverses:", somme_inverses)
