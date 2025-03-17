'''
Verificar si un input es un número: Usa try-except para asegurarte de que el usuario ingresa un número.
'''
def verificar_numero():
    while True:
        try:
            numero = float(input("Ingrese un número: "))
            return numero
        except ValueError:
            print("Error: Por favor, ingrese un número.")
print("Jesus Sanchez Rodriguez")    