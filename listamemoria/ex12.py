# Projete uma função que receba duas listas como parâmetro e modifique a primeira lista adicionando todos os elementos da segunda lista no final da primeira.

def adiciona_lista(lst1: list[int], list2: list[int]) -> None:
    '''
    >>> lst1 = [1,2,3,4]
    >>> lst2 = [1,2,3,4]
    >>> adiciona_lista(lst1, lst2)
    >>> print(lst1)
    [1, 2, 3, 4, 1, 2, 3, 4]

    >>> lst1 = []
    >>> lst2 = [1,2,3,4]
    >>> adiciona_lista(lst1, lst2)
    >>> print(lst1)
    [1, 2, 3, 4]

    >>> lst1 = [1,2,3,4]
    >>> lst2 = []
    >>> adiciona_lista(lst1, lst2)
    >>> print(lst1)
    [1, 2, 3, 4]

    >>> lst1 = []
    >>> lst2 = []
    >>> adiciona_lista(lst1, lst2)
    >>> print(lst1)
    []
    '''

    for i in list2:
        lst1.append(i)