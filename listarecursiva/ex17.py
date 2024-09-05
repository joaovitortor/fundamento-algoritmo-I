# (Desafio) Projete uma função recursiva que verifique se uma lista é palíndromo. Dica: diminua do
# início e do final.

def palindromo(lst: list[int], inicio: int, fim: int) -> bool:
    if len(lst) % 2 == 0:
        if inicio == fim-1:
            if lst[inicio] == lst[fim]:
                eh_palindromo = True
            else: 
                eh_palindromo = False
        else:
            if lst[inicio] != lst[fim]:
                eh_palindromo = False
            else:
                eh_palindromo = palindromo(lst, inicio+1, fim -1)
    else:
        if inicio == fim:
            eh_palindromo = True
        else:
            if lst[inicio] != lst[fim]:
                eh_palindromo = False
            else:
                eh_palindromo = palindromo(lst, inicio+1, fim -1)        
    return eh_palindromo

lst = [3,2,1,3,3]
print(palindromo(lst, 0, len(lst)-1))