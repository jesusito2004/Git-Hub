'''
    Ejercicio de clase.

    Crear una clase Empleado que modele trabajadores con un nombre y apellidos, un cargo y un salario.
    El salario debe ser (obligatoriamente) un atributo privado.

'''
class Empleado:
    def __init__(self, nombre, cargo, salario):
        self.nombre = nombre
        self.cargo = cargo
        self.__salario = salario  # Atributo privado

    # Método para obtener el salario
    def get_salario(self):
        return self.__salario

    # Método para representar el objeto como cadena
    def __str__(self):
        return f"Nombre: {self.nombre}, Cargo: {self.cargo}, Salario: {self.__salario}"

# Lista de empleados
listaEmpleados = [
    Empleado("Juanma", "Director", 75000),
    Empleado("Teresa", "Presidenta", 80000),
    Empleado("Ana", "Administrativo", 25000),
    Empleado("Mario", "Conserje", 20000)
]

# Seleccionar empleados con salario > 50k
empleados_vip = [emp for emp in listaEmpleados if emp.get_salario() > 50000]

# Mostrar los empleados VIP
for ev in empleados_vip:
    print(ev)

print("Jesús Sánchez Rodríguez")