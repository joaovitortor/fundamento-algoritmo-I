# Ordenação por seleção

def ordena_selecao(lst: list[int]) -> None:
    for i in range(len(lst)):
        while i > 0 and lst[i - 1] > lst[i]:
            # troca lst[i] <-> lst[i - 1]
            t = lst[i]
            lst[i] = lst[i - 1]
            lst[i - 1] = t
            i = i - 1

lista = [8, 5, 4, 1, 2]
ordena_selecao(lista)
print(lista)

# tenho que fazer alguma coisa para cortar a lista na repetição