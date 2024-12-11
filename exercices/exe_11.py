capital = float(input("Veuillez saisir votre capital: "))
taux = float(input("Veuillez saisir le taux en %: "))

annee = 1
cn = 0
gain = 0
while gain < 2* capital:
    cn = (capital*(1+(taux/100))) ** annee
    gain = capital - cn
    annee += 1

print("nb d'annees", annee)