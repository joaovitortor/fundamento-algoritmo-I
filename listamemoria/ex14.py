# Projete uma função que receba como parâmetros uma lista e um índice i e modifique a lista removendo o elemento do índice i

def remove_indice(lst: list[int], i: int) -> None:
    '''
    
    >>> lst = [1, 2, 3, 4, 5]
    >>> remove_indice(lst, 2)
    >>> print(lst)
    [1, 2, 4, 5]
    '''
    while i < len(lst) -1:
        t = lst[i]
        lst[i] = lst[i + 1]
        lst[i + 1] = t
        i = i + 1

    lst.pop()
