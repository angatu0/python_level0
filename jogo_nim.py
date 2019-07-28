def partida():
    n = int(input('Quantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    Ch = 0
    if n % (m + 1) == 0:
        print('\nVocê começa!')
        n -= Ch
        pcGO = False
    else:
        print('\nComputador começa!')
        n -= Ch
        pcGO = True
    while n > 0:
        if pcGO:
            Ch = computador_escolhe_jogada(n, m)
            if n-Ch != 0:
                print('\nO computador tirou {} peças'.format(Ch))
                print('Agora restam {} peças no tabuleiro.'.format(n-Ch))
            else:
                print('\nO computador tirou {} peças'.format(Ch))
            pcGO = False
        else:
            Ch = usuario_escolhe_jogada(n, m)
            print('\nVocê retirou {} peças.'.format(Ch))
            print('Agora restam {} peças no tabuleiro.'.format(n-Ch))
            pcGO = True
        n -= Ch
    if pcGO:
        print('Você ganhou!!')
        return 1
    else:
        print('Fim do jogo! O computador ganhou!')
        return 0
def computador_escolhe_jogada(n, m):
    if n <= m:
        return n
    else:
        ce = n % (m+1)
        if ce > 0:
            return ce
    return m
def usuario_escolhe_jogada(n, m):
    ue = 0
    while ue == 0:
        ue = int(input('\nQuantas peças você vai tirar? '))
        if ue > m or ue <= 0 or ue > n:
            print('\nOops! Jogada inválida! Tente de novo.')
            ue = 0
        else:
            return ue
def campeonato():
    nR = 1
    print('\n**** Rodada {} ****'.format(nR))
    rodada = partida()
    while nR < 3:
        print('\n**** Rodada {} ****'.format(nR+1))
        partida()
        if rodada == 1:
            nR += 1
        else:
            nR += 1
    if nR == 3:
        print('\n**** Final de campeonato! ****')
        print('\nPlacar: Você 0 x 3 Computador')
print('Bem-vindo ao jogo do NIM! Escolha:')
op = 0
while op == 0:
    op = int(input('1 - para jogar uma partida isolada\n2 - para jogar um campeonato'))
    if op == 1:
        print('\nVoce escolheu partida única')
        partida()
        break
    elif op == 2:
        print('\nVoce escolheu um campeonato!')
        campeonato()
    else:
        print('Opção Inválida')
        op = 0