cuantos = int(input("Cuantos usuarios van a crear?"))

usuarios = []
for i in range(cuantos):
    nombre = input("Ingrese el nombre del usuario")
    usuarios.append(nombre)
    print(usuarios)