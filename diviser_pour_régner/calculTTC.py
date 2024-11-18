def calculTTC(nba,prix,taxe):
    return nba*prix*(1+taxe/100)

print(calculTTC(5,42.15,19.6))