# Projete uma função recursiva que concatene todas as strings de uma lista.

def concatena_str(lst: list[str]) -> str:
    if lst == []:
        concatena = ''
    else:
        concatena = lst[0] + concatena_str(lst[1:])
    return concatena

lst = ['a','b','c']
print(concatena_str(lst))