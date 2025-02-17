

def imprime_pares(lista):
    '''
    toma como un argumento una lista de numeros e imprime solamente los pares
    '''

    for num in lista:
        if int(num) % 2 == 0:
            print(num)
        else:
            continue    