# sumador de numeros



from imprime_pares import imprime_pares as impp

'''
    este programa toma una serie de numeros como entrada 
    y devuelve la suma de todos los numeros en la serie
    si encuentra caracteres no numericos, lanza una excepcion

'''

line = input("Ingresa una linea de numeros, separalos con espacios: ")
strings = line.split()
total = 0
try:
    for string in strings:
        total += int(string)
        print(total)
except:
    print("Error," +string+ " no se pudo convertir a entero")  # si no se puede


impp(strings)    