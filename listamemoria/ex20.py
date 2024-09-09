def junta_nome(lst: list[str]) -> str:
    '''
    
    >>> junta_nome(['joao','vitor','bidoia'])
    'joao vitor bidoia'
    '''
    if len(lst) == 1:
        nome = lst[0]
    else:
        nome = lst[0] + ' ' + junta_nome(lst[1:])
    return nome

def maximo_caractere(lst: list[list[str]]) -> int:
    '''
    

    >>> maximo_caractere([['joao','vitor','bidoia'],['joao','vitor']])
    17
    '''
    if len(lst) == 1:
        maior = len(junta_nome(lst[0]))
    else: 
        maior = max(len(junta_nome(lst[0])), maximo_caractere(lst[1:]))

    return maior


lista = ['s']
lista = ['s'] + ['a']
print(lista)