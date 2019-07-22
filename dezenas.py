n = int(input('Digite um numero inteiro positivo: '))
    #"n" é o numero inteiro positivo que será digitado
un = n % 10
    #Primeiro, acho a unidade que será o resto da divisão por dezena
n = (n - un)/10
    #Aqui eu atualizo o valor de "n" sem a unidade
dez = int (n % 10)
    #vAque você repete o processo da unidade para achar o valor da DEZENA
n = (n - dez)/10
    #Essa seria para achar a centena. Mas não está sendu usada abaixo

print('O dígito das dezenas é {}.'.format(dez))
    #Aqui pedimos para imprimir a dezena encontrada na variável "dez"
