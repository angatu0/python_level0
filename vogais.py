def vogal(x):
    vogais = ('a', 'A', 'e', 'E', 'i', 'I',  'o', 'O', 'u', 'U')
    for v in range (0, len(vogais)):
        if x == vogais[v]:
            return True
    return False