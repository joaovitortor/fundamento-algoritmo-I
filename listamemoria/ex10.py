# Projete uma função que modifique uma lista de números somando um valor n a cada um dos seus elementos

def soma_n(lst: list[int], n: int) -> None:
    '''
    Modifica a lista *lst* somando *n* em cada um dos seus elemetos

    >>> lst = []
    >>> soma_n(lst, 5)
    >>> print(lst)
    []

    >>> lst = [1, 2, 3]
    >>> soma_n(lst, 5)
    >>> print(lst)
    [6, 7, 8]
    '''

    for i in range(0, len(lst)):
        lst[i] = lst[i] + n