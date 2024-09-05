#  Projete uma função que modifique uma lista de strings deixando todas com o mesmo tamanho. Adiciona espaços em branco ao final das strings se necessário.

def str_n(lst: list[str], n: int) -> None:
    '''
    Modifica os elementos de *lst*, deixando as str do mesmo tamanho *n*

    >>> lst = []
    >>> str_n(lst, 3)
    >>> print(lst)
    []

    >>> lst = ['alou', 'joao', 'pedro']
    >>> str_n(lst, 3)
    >>> print(lst)
    ['alo', 'joa', 'ped']

    >>> lst = ['', 'a', 'b']
    >>> str_n(lst, 3)
    >>> print(lst)
    ['   ', 'a  ', 'b  ']

    '''

    for i in range(0, len(lst)):
        if len(lst[i]) < n:
            espaco = ' ' * (n - len(lst[i]))
            lst[i] = lst[i] + espaco
        elif len(lst[i]) > n:
            lst[i] = lst[i][:n]