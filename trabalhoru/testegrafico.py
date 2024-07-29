from dataclasses import dataclass
from enum import Enum, auto

class Usuarios(Enum):
    '''
    Representa o ********. 
    **, ** e ** devem ser tal coisa. * e * devem ser menores que 60.
    '''
    ALUNO = auto()
    SERVIDOR_ATE3 = auto()
    SERVIDOR_MAIOR3 = auto()
    DOCENTE = auto()
    EXTERNO = auto()

class Pagamento(Enum):
    '''O tipo do pagamento na venda'''
    DINHEIRO = auto()
    PIX = auto()
    CARTAO = auto()

@dataclass
class Venda:
    usuario: Usuarios
    pagamento: Pagamento
    quantidade: int

def valor_usuario(tipo_usuario: Usuarios) -> int:
    '''
    Retorna o valor do tiquet do usuario selecionado pelo *tipo_usuario*

    >>> tipo_usuario(1)
    5
    >>> tipo_usuario(2)
    5
    >>> tipo_usuario(3)
    10
    >>> tipo_usuario(4)
    10
    >>> tipo_usuario(5)
    19
    '''

    if tipo_usuario == Usuarios.ALUNO or tipo_usuario == Usuarios.SERVIDOR_ATE3:
        valor = 5
    elif tipo_usuario == Usuarios.SERVIDOR_MAIOR3 or tipo_usuario == Usuarios.DOCENTE:
        valor = 10
    else:
        valor = 19
    return valor

def contar_usuario(vendas: list[Venda], usuario: Usuarios) -> int:
    '''
    
    
    >>>
    
    '''
    quant_usuario = 0
    for Venda in vendas:
        if Venda.usuario == usuario:
            quant_usuario = quant_usuario + 1
    return quant_usuario

def contar_pagamento(vendas: list[Venda], pagamento: Pagamento) -> int:
    '''
    
    
    >>>
    
    '''
    quant_pagamento = 0
    for Venda in vendas:
        if Venda.pagamento == pagamento:
            quant_pagamento = quant_pagamento + Venda.quantidade * valor_usuario(Venda.usuario)
    return quant_pagamento

def maior(a: int, b: int) -> int:
    maior = 0
    if a > b:
        maior = a
    else:
        maior = b
    return maior

def main():
    alunos = 50
    servidor_ate3 = 10
    servidor_maior3 = 5
    docente = 30
    externo = 5

    total = alunos + servidor_maior3 + servidor_ate3 + docente + externo

    porc_alunos = alunos / total * 100
    porc_servidor_ate3 = servidor_ate3 / total * 100
    porc_servidor_maior3 = servidor_maior3 / total * 100
    porc_docente = docente / total * 100
    porc_externo = externo / total * 100

    print('aluno =      ', '*' * (int(porc_alunos // 5)))
    print('Servidor<3 = ', '*' * (int(porc_servidor_ate3 // 5)))
    print('Servidor>3 = ', '*' * (int(porc_servidor_maior3 // 5)))
    print('docente =    ', '*' * (int(porc_docente // 5)))
    print('externo =    ', '*' * (int(porc_externo // 5)))
 

if __name__ == '__main__':
    main()
