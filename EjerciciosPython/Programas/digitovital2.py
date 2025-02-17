
fecha = ''

while True:
    fecha = input("Ingrese la fecha de nacimiento (dd/mm/aaaa): ")
    if fecha.isnumeric():
        break
    print("Debes de introducir una fecha en formato AAAAMMDD.")


digito = 0
suma = 0

for c in fecha:
    suma += int(c)

if suma < 10:
    digito = suma
else:
    for c in str(suma):
        digito += int(c)

print('El numero vital es ', digito)
    
       
