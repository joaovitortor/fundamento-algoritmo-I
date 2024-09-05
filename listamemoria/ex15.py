# Projete uma função que modifique uma lista removendo todos os elementos que estão em índices pares.

def remove_indice_par(lst: list[int]) -> None:
    for i in range(len(lst) -1, -1, -1):
        if i % 2 == 0:
            indice = len(lst)
            while i < len(lst)-1:
                t = lst[i+1]
                lst[i+1] = lst[i]
                lst[i] = t
                i = i+1
            lst.pop()

        

lst = [0,1,0,1,0,1]
remove_indice_par(lst)
print(lst)
