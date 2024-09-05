# Projete uma função recursiva que receba como parâmetro um número natural n e calcule o produto dos números 1, 2, · · · , n.

def fatorial(n: int) -> int:
    '''
    
    >>> fatorial(5)
    120
    '''
    if n == 1:
        soma = 1
    elif n > 1:
        soma = n * fatorial(n-1)
    return soma