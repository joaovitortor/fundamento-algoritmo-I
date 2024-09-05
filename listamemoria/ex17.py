# Projete uma função que modifique uma lista colocando os valores menores ou iguais a zero antes dos valores maiores que zero

def ordena_lista(lst: list[int]):
    for i in range(0, len(lst)):
        if lst[i] < 0:
            while i > 0:
                t = lst[i]
                lst[i] = lst[i-1]
                lst[i-1] = t
                i = i -1
            
lst = [10, -5, 98, -96, 5, -9]
ordena_lista(lst)
print(lst)
