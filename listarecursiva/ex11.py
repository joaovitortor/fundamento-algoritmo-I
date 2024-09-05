#  Projete uma função recursiva que determine se um número está em uma lista de números

def numero_lst(lst: list[int], n: int) -> bool:
    if lst == []:
        incluso = False
    else:
        if lst[0] != n:
            incluso = numero_lst(lst[1:], n)
        else:
            incluso = True
    return incluso

lst = [1,2,3,4,5,6]
print(numero_lst(lst, 7))