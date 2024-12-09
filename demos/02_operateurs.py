from math import *
nb = pi

# import math
# pi = math.pi

# Addition
a = 10 + 12
# Division
a = 10 / 12
# Division entiére
a = 10 // 12
# modulo
a = 10 % 12
# multiplication
a = 10 * 12
# puissance de 
a = 10 ** 12
# soustraction
a = 10 - 12

b = 10
# sol 1 :
b = b - 5 
# sol 2 :
b-=5

nba = input("Saisir un nombre a: ")
nbb = input("Saisir un nombre b: ")

# concaténation de a et b 
print(nba + nbb)
# la multiplication  sur une chaine de cacar duplique celle-ci
print(nba * 15)

# les ope de comparasion
print("-" * 100)
print(nba>nbb)
print(nba<nbb)
print(nba<=nbb)
print(nba>=nbb)
print(nba==nbb)
print(nba!=nbb)

# les ope de logique
print("-" * 100)
print((25<5) and not (18>98))
print((25>5) or not (18>98))
