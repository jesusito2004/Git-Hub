



palabra = input("Introduce palabra a buscar: ").upper()
grupo  = input("Introduce palabra a buscar: ").upper()

contiene = True
inicio = 0 

for c in palabra:
    posicion = grupo.find(c)
    if posicion < 0:
        contiene = False
        break
    else:
        contiene = True

if contiene:
    print("La palabra se encuentra en el grupo")
else:
    print("La palabra no se encuentra en el grupo")
  