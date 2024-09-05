# Uma lista de números é chamada de lista binária se todos os seus elementos são 0 ou 1. Projete uma
# função recursiva que verifique se uma lista é binária.

def lst_binaria(lst: list[int]) -> bool:
    if lst == []:
        eh_binaria = False
    elif len(lst) == 1:
        if lst[0] != 1 and lst[0] != 0:
            eh_binaria = False
        else:
            eh_binaria = True
    else:
        if lst[0] != 1 and lst[0] != 0:
            eh_binaria = False
        else:
            eh_binaria = True and lst_binaria(lst[1:])
            
    return eh_binaria

