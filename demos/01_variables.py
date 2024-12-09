# Afficher le message dans le console
# ctrl + ":" permet de commenter/decom une ligne rapidement
# pour dupliquer alt + shift + fleche de bas
# pour informer le type de variable on peut metre aprés le nom du variable le type comme var : int/str/bool...
print("Hello!")

print("--------------------------")
print("Les variables: ")

# Pour déclarer une variable : 
ma_variable= 8
ma_variable = ma_variable * 2 

# Pour utiliser ma variable:
print(ma_variable)

# types numériques : 
var = 23
var = 23
print(type(var))

# types chaine de carac
var = "ma chaîne"
print(type(var))

#type booléens:
var = True
var = False

# récuprer une variable
nb_a = input("Veuillez saisir une valeur: ")
print("le nombre est: ",nb_a)

# cast de variable
nb = int(nb_a)
print(type(nb))

# cast et input au m temps
nb_b = int (input("Veuillez saisir une valeur: "))

# formater une phrase
print(f"le nombre a est: {nb_a:^7.2f}, le nombre b est: {nb_b:^7.2f}")



