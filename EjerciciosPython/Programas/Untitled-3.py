
text = input("Ingresa tu mensaje:")
cipher = ''

while True:
    num = input("Introduce el desplazamiento")
    if num in range(1,25):
        break
for char in text:
    if not char.isalpha():
        continue
    char = char.upper()
    