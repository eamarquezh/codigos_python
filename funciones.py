def imprimir_mensaje(eleccion):
    print("hola has elegido la opcion " + str(eleccion))

opcion = int(input("hola elige una opcion"))

if opcion == 1:
    imprimir_mensaje(opcion)
    print("acciones opcion 1")
if opcion == 2:
    imprimir_mensaje(opcion)
    print("acciones opcion 1")
else:
    print("elige una opcion valida")