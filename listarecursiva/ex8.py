# Projete uma função recursiva que receba como parâmetro um número natural n e gere uma string com os números de 1 até n separados por vírgula. Por exemplo, para n = 3, a função deve gerar "1,2,3".

def gera_str(n: int) -> str:
    if n == 1:
        texto = str(n)
    elif n > 1:
        texto = gera_str(n-1) + ',' + str(n)
    return texto

print(gera_str(5))