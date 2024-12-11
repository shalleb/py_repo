i = 0
while i < 10 :
    i += 1

    if i == 3:
        print("Ma variable est à 3")
    
    if i == 2:
        continue

    if i == 7:
        break
print("Hello", i)

print("-" * 50)

for i in range(0,10,2):
    print("I'm", i)

chaine = "test d'une chaine de carac"

i=0
for lettre in chaine:
    if lettre == "c":
        i += 1
print(f"il y a {i} c dans la chaine")


