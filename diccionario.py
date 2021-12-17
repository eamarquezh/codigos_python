def run():
    mi_diccionario ={
        'llave1':1,
        'llave2':2,
        'llave3':3,
        'llave4':4
    }
    for llaves in mi_diccionario.keys():
        print(llaves)
    for valores in mi_diccionario.values():
        print(valores)
    for llaves,valores in mi_diccionario.items():
        print(llaves + ":" + str(valores))


if __name__ == '__main__':
    run()