def hello_world():
    print("Hello world! ")

hello_world()

def addition (a : int, b : int) -> int:
    try:
        resultat = a + b 
        return resultat
    except Exception as e:
        print(e)

a = input("Donnez un nombre a: ")
b = input("Donnez un nombre b: ")
res = addition(a,b)
print("resultat addition est: ",res)

