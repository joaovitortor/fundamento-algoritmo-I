# (Desafio) Projete uma função recursiva que altere uma lista invertendo a ordem dos seus elementos

def inverte_lista(lst: list[int], inicio: int, fim: int) -> None:
    assert inicio >= 0 and fim < len(lst)
    if inicio < fim:
        t = lst[fim]
        lst[fim] = lst[inicio]
        lst[inicio] = t
        inverte_lista(lst, inicio + 1, fim -1)
    
lst = [9,8,7,6]
inverte_lista(lst, 0, len(lst)-1)
print(lst)