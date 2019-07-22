def maior_primo(k):
    contador = k
    x = 0
    while contador >= 1:
        for x in range(2, k + 1):
            if contador % x == 0:
                break
        if x == contador:
            return x
        contador -= 1
        return maior_primo(contador)


