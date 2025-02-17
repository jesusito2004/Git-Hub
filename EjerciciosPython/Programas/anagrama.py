
while True:

    text1 = str(input("Introduce la primer palabra")).upper()
    if not text1.isapha():
        print("La palabra no es alfabética")
        break
    else:
        text2= input("Introduce la segunda palabra").upper()
        if not text2.isalpha():
            print("La palabra no es alfabética")
            break

if sorted(text1) == sorted(text2):
    print("Las palabras son iguales")
else:
    print("Las palabras son diferentes")
        