# escreva o seu programa
def main():
    n = int(input('Digite o valor: '))
    soma = 0

    while n != 0:
        soma = soma + n
        n = int(input('Digite o valor: '))

    print('A soma é {}'.format(soma))


main()