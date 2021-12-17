def run():
    # for contador in range(1000):
    #     # if contador % 2 != 0:
    #     #     continue
    #     # print(contador)
    #     # if contador == 500:
    #     #     break
    #     # print(contador)
    texto = input("Escribe un texto: ")
    for letra in texto:
        if letra == "o":
            break
        print(letra)


if __name__ == '__main__':
    run()