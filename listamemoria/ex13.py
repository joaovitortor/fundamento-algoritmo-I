# Projete uma função que receba como parâmetros uma lista, um índice i e um valor v, e modifique a lista inserindo o valor v no índice i. Dica: veja o exemplo insere_ordenado

def insere_valor_indice(lst: list[int], i: int, v: int) -> None:
    '''
    ...
    
    >>> lst = [1, 2, 3, 4]
    >>> insere_valor_indice(lst, 2, 5)
    >>> print(lst)
    [1, 2, 5, 3, 4]

    
    '''
    lst.append(v)
    indice = len(lst) - 1
    while indice > i:
        t = lst[indice]
        lst[indice] = lst[indice-1]
        lst[indice-1] = t
        indice = indice - 1




