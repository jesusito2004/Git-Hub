'''
Instalar y usar un paquete con PIP: Instala requests y úsalo para obtener el contenido de una página web.
'''

import requests
response = requests.get('https://www.example.com')
print(response.text)

print("Jesús Sánchez Rodríguez")