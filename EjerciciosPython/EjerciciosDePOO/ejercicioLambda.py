"""

"""


ataques_base = [30, 55, 40, 75, 20]

ataques_modificados = list(map(lambda x: x * 1.2 if x > 50 else x, ataques_base))

print("Ataques mejorados:", ataques_modificados)