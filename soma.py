print('Hora de dividir a conta. Digite os valores a serem somados e digite "0" para concluir')
soma = 0
valor = 1
while valor != 0:
    valor = float(input('Digite o valor aqui > R$ '))
    soma = soma + valor
p = float(input('Digite o número de pessoas que vão dividir a conta: '))
print(input('O total foi de R$ {}. Ficará R$ {:.2f} para cada pessoa'.format(soma,(soma/p))))
