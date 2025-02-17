

frase = input("Introduce tu frase:")

frase2 = input(frase.lower()).replace(' ','')


if frase2 == frase2[::-1]:
    print("La frase es un palíndromo")
else:
    print("La frase no es un palíndromo")