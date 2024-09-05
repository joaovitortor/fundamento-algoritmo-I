# Projete uma função recursiva que receba como parâmetro um número natural n e um valor v e crie uma nova lista com n repetições do valor v.

def repete_n(n: int, v: int, lst: list[int] = []) -> list[int]:
    '''
    

    >>> repete_n(10, 5)
    [10, 10, 10, 10, 10]
    '''
    if v == 0:
        lst = []
    elif v > 0:
        lst.append(n)
        repete_n(n, v-1, lst)
    return lst
