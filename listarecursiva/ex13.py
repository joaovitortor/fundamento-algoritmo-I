# Projete uma função recursiva que encontre o valor máximo de uma lista não vazia. Dica: mude o caso
# base para uma lista com um elemento

def maximo(lst: list[int], maior: int = 0) -> int:
    assert len(lst) > 0
    if len(lst) == 1:
        m = lst[0]
    else:
        m = max(lst[0], maximo(lst[1:]))
    return m

print(maximo([1,5,9,12,3,4]))