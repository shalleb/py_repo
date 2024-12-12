# ma_liste = []
# i=0
# while i < 10:
#     ma_liste.append((input(f"Donnez le {i+1} chiffre: ")))
#     i+=1

# liste compréhension
liste = [i for i in range(1,11)]
print(liste)

# print("mon 9éme element est: ",ma_liste[8])

# print("-"*50)
# liste_notes = []
# i=0
# while i < 15:
#     liste_notes.append((input(f"Donnez la note n°{i+1}: ")))
#     i+=1

# i=1
# for item in (liste_notes):
#     print(f"la {i} note est : {item}")
#     i+=1

print("-"*50)

def saisie_notes():
    liste_notes=[]
    while True:
        note = (int(input(f"Veuillez entrer une note entre 0 et 20 compris (une note négtaive stoppera la saisie): ")))
        if note < 20:
            liste_notes.append(note)
            if (note < 0) :
                liste_notes.remove(note)
        break
        
    print(liste_notes)



saisie_notes()