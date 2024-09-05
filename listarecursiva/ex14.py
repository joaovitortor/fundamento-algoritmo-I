# Projete uma função recursiva que encontre o tamanho máximo entre todas as strings de uma lista de strings.

def maximo_str(lst: list[str], n: int) -> int:
    if n == 0:
        maximo = 0
    else:
        maximo = max(len(lst[n]), maximo_str(lst, n-1))
    return maximo

lst = ['abc', '1', '1235', '12']
print(maximo_str(lst, len(lst)-1))