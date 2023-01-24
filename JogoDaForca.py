secreto = 'clube'
digitadas = []
chances = 7
registro_letras = []

print('A palavra é : ', len(secreto) * '*')
while True:
    if chances == 0:
        print("Você perdeu!!")
        break

    letra = input("Digite um letra: ")

    if len(letra) > 1:
        print("AAAAAA, isso não vale, digite apenas uma letra. ")
        continue

    if letra in digitadas:
        print("Essa letra já foi utilizada")

    else:
        digitadas.append(letra)

        if letra in secreto:
            print("BOA, a letra ", letra, "existe na palavra secreta. ")
        else:
            print("DROGA!, a letra", letra, "não existe na palavra secreta. ")
            digitadas.pop()

        secreto_temporario = ""
        for letra_secreta in secreto:
            if letra_secreta in digitadas:
                secreto_temporario += letra_secreta
            else:
                secreto_temporario += "*"

        if secreto_temporario == secreto:
            print("Que legal, VOCÊ VENCEU!!!, a palavra era ",
                  secreto_temporario, ".")
            break
        else:
            print("A palavra secreta está assim: ", secreto_temporario)

        if letra not in secreto:
            chances -= 1
        registro_letras.append(letra)
        print("Você ainda tem", chances, "chances")
        print("As letras digitadas foram: ", registro_letras)
        print()
