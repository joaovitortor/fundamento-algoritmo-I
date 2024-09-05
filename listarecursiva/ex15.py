# Projete uma função recursiva que crie uma nova lista com todos os valores positivos de uma lista de números.

def valor_postivo(lst: list[int], n: int, lista_positivo: list[int] = []) -> list[int]:
    if n == 0:
        lista_positivo = []
    else:
        if lst[n] > 0:
            lista_positivo.append(lst[n])
        valor_postivo(lst, n - 1, lista_positivo)

    return lista_positivo

lst =[-1,2,-5,9,8,-99]
print(valor_postivo(lst, n = len(lst) - 1))