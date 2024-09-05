# Recursão indireta é quando duas ou mais funções chamam uma a outra. Defina duas funções impar e
# par, uma em termos da outra, isto é, a função impar deve chamar a função par e a função par deve
# chama a função impar (a recursão para no caso base).

def par(n: int) -> bool:
    if n == 0:
        par = True
    elif n > 0:
        par = impar(n-1)
    return par

def impar(n: int) -> bool:
    if n == 0:
        impar = False
    elif n > 0:
        impar = par(n-1)
    return impar

print(impar(5))