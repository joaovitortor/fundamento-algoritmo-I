# Projete uma função que modifique uma lista de strings removendo todas as strings vazias.

def remove_vazio(lst: list[str]) -> None:
    for i in range(len(lst) - 1, -1, -1):
        if lst[i] == '':
            while i < len(lst) - 1:
                t = lst[i + 1]
                lst[i+1] = lst[i]
                lst[i] = t
                i = i + 1
            lst.pop()


lst = ['', 'a', '']
remove_vazio(lst)
print(lst)