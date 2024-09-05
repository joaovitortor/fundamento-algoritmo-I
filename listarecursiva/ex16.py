# Projete uma função recursiva que altere uma lista somando 1 em cada um dos seus elementos.

def soma_1(lst: list[int], n: int) -> None:
    if n >= 0 and n < len(lst):
        lst[n] = lst[n] + 1
        soma_1(lst, n-1)

lst = [1,2,3,4,5]
soma_1(lst, len(lst)-1)
print(lst)