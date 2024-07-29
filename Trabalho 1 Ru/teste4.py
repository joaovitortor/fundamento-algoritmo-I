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

def main() -> None:
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

            if escolha_usuario > 0 and escolha_usuario < 6:

                quant_tiquet = int(input('Quantos tiquetes estão sendo comprados? '))

                print('|====================|')
                print('| Forma de pagamento |')
                print('|(1) Dinheiro        |')
                print('|(2) Pix             |')
                print('|(3) Cartao          |')
                print('|====================|')

                forma_pagamento = int(input('Selecione o método de pagamento: '))
                if forma_pagamento > 0 and forma_pagamento < 4:

                    vendas.append(Venda(tipo_usuario(escolha_usuario), tipo_pagamento(forma_pagamento), quant_tiquet))
                    total = quant_tiquet * valor_usuario(tipo_usuario(escolha_usuario))
                    print('===========================')
                    print('Venda realizada com sucesso')
                    print('Usuario:', tipo_usuario(escolha_usuario).name)
                    print('Quantidade de tiquet:', quant_tiquet)
                    print('Total:', total)
                    print('===========================')

        elif operacao == 2:
            print(vendas)
            print('Alunos: ', contar_usuario(vendas, Usuarios.ALUNO))
            print('Servidor<3: ', contar_usuario(vendas, Usuarios.SERVIDOR_ATE3))
            print('Servidor>3: ', contar_usuario(vendas, Usuarios.SERVIDOR_MAIOR3))
            print('Docente: ', contar_usuario(vendas, Usuarios.DOCENTE))
            print('Externo: ', contar_usuario(vendas, Usuarios.EXTERNO))
            print('Cartão: ', contar_pagamento(vendas, Pagamento.CARTAO))
            print('Dinheiro: ', contar_pagamento(vendas, Pagamento.DINHEIRO))
            print('Pix: ', contar_pagamento(vendas, Pagamento.PIX))


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
    Analisa qual elemento da classe enumerada foi selecionado pela *escolha_usuario*
    
    >>> tipo_usuario(1).name
    'ALUNO'
    >>> tipo_usuario(2).name
    'SERVIDOR_ATE3'
    >>> tipo_usuario(3).name
    'SERVIDOR_MAIOR3'
    >>> tipo_usuario(4).name
    'DOCENTE'
    >>> tipo_usuario(5).name
    'EXTERNO'

    '''
    if escolha_usuario == 1:
        tipo_usuario = Usuarios.ALUNO
    elif escolha_usuario == 2:
        tipo_usuario = Usuarios.SERVIDOR_ATE3
    elif escolha_usuario == 3:
        tipo_usuario = Usuarios.SERVIDOR_MAIOR3
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
