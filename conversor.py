def convertir(conversor,valor_dolar):
    pesos = input("¿cuantos pesos " + conversor + " tienes?")
    pesos = float(pesos)
    valor_dolar = valor_dolar
    dolares = pesos / valor_dolar
    dolares = round(dolares,2)
    dolares= str(dolares)
    print("tienes " + dolares + " dolares")

menu = """
Bienvenidos al conversor de monedas:

1 - pesos colombianos
2 - pesos argrentinos
3 - pesos mexicanos
"""
opcion = int(input(menu))

if opcion == 1:
    convertir("colombianos",3093)
elif opcion == 2:
    convertir("argentinos",101)
    pesos = input("¿cuantos pesos argentinos tienes?")
elif opcion == 3:
    convertir("mexicanos",20)
else:
    print("Escribe una opcion")