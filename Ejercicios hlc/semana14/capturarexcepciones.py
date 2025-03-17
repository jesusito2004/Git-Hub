'''
Capturar múltiples excepciones: Maneja errores si el usuario intenta abrir un archivo inexistente o dividir entre 0.
'''
try:
    archivo = open('archivo.txt', 'r')
    contenido = archivo.read()
    archivo.close()
    print(contenido)
except FileNotFoundError:
    print('El archivo no existe')
except ZeroDivisionError:
    print('No se puede dividir entre 0')
except Exception as e:
    
    print(f'Ocurrió un error: {e}')
