import math


def aire(h,w):
    return h*w;

def volume_shere(rayon):
    return 4/3 * math.pi * rayon**3

#aire d'un rectangle
"""w = float(input("donnez le largeur: "))
h = float(input("donnez le lengeur: "))
air = aire(h,w)
txt = "l'aire de rectangle de langeur : {largeur:^2} et longeur : {longeur:^2} est {air:^2}"
print(txt.format(largeur=w , longeur=h , air=air))"""

#volume d'une sphére
rayon = float(input("donnez le rayon: "))
volume = volume_shere(rayon)
txt = "le volume d'une sphére qui avoir une rayon de {r} est {v}"
print(txt.format(r=rayon, v=volume))
print('%.3f'%rayon)