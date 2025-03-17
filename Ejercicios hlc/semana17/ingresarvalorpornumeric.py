try:
    # Ingresar un valor por teclado
    valor = input("Ingrese un valor: ")

    # Intentar convertir el valor a un número
    if valor.isnumeric():
        print("El valor ingresado es numérico.")
    else:
        raise ValueError("El valor ingresado no es numérico.")
except ValueError as e:
    print(e)
print("Jesús Sánchez Rodríguez") 