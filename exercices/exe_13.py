tmp = 
for i in range (1,6):
    nombre = float(input(f"Veuillez saisir le {i} nombre : "))
    if (nombre > tmp ):
        tmp = nombre
print(f"le nombre le plus grand est: ",tmp)