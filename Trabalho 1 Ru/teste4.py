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

def main():
    operacao = 0
    vendas = []
    while operacao != 3:
        print('========================')
        print('|     OPERAÇÕES        |')
        print('| (1) Registrar venda  |')
        print('| (2) Exibir relatório |')
        print('| (3) Encerrar         |')
        print('========================')

        operacao = int(input('Escolha a opção desejada inserindo o número: '))

        if operacao == 1:
            print('=====================')
            print('|  Tipo de Usuario  |')
            print('| (1) Aluno         |')
            print('| (2) Servidor<=3   |')
            print('| (3) Servidor>3    |')
            print('| (4) Docentes      |')
            print('| (5) Externo       |')
            print('| (6) Cancelar      |')
            print('=====================')

            escolha_usuario = int(input('Escolha o usuario desejado inserindo o número: '))

            if escolha_usuario > 0 and escolha_usuario < 7:

                usuario = tipo_usuario(escolha_usuario)
                quant_tiquet = int(input('Quantos tiquetes estão sendo comprados? '))

                print('|====================|')
                print('| Forma de pagamento |')
                print('|(1) Dinheiro        |')
                print('|(2) Pix             |')
                print('|(3) Cartao          |')
                print('|====================|')

                forma_pagamento = int(input('Selecione o método de pagamento: '))
                if forma_pagamento > 0 and forma_pagamento < 4:
                    pagamento_enum = tipo_pagamento(forma_pagamento)
                    vendas.append(Venda(usuario, pagamento_enum, quant_tiquet))
                    print('===========================')
                    print('Venda realizada com sucesso')
                    print('Usuario:', usuario.name)
                    print('Quantidade de tiquet:', quant_tiquet)
                    print('Total:', quant_tiquet * valor_usuario(usuario))
                    print('===========================')

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

def tipo_usuario(escolha_usuario: int) -> Usuarios:
    '''
    
    
    >>>

    '''
    if escolha_usuario == 1:
        tipo_usuario = Usuarios.ALUNO
    elif escolha_usuario == 2:
        tipo_usuario = Usuarios.SERVIDOR_ATE3
    elif escolha_usuario == 3:
        tipo_usuario = Usuarios.SERVIDOR_ATE3
    elif escolha_usuario == 4:
        tipo_usuario = Usuarios.DOCENTE
    elif escolha_usuario == 5:
        tipo_usuario = Usuarios.EXTERNO
    return tipo_usuario

def tipo_pagamento(forma_pagamento) -> Pagamento:
    '''
    
    
    >>>
    
    '''
    if forma_pagamento == 1:
        forma_pagamento = Pagamento.DINHEIRO
    elif forma_pagamento == 2:
        forma_pagamento = Pagamento.PIX
    elif forma_pagamento == 3:
        forma_pagamento = Pagamento.CARTAO
    return forma_pagamento

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

if __name__ == '__main__':
    main()
