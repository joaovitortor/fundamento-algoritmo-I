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

            tipo_usuario = int(input('Escolha o usuario desejado inserindo o número: '))

            if tipo_usuario > 0 and tipo_usuario < 7:

                valor = valor_usuario(tipo_usuario)
                tipo_usuario = tipo_usuario(tipo_usuario)
                quant_tiquet = int(input('Quantos tiquetes estão sendo comprados? '))

                print('|====================|')
                print('| Forma de pagamento |')
                print('|(1) Dinheiro        |')
                print('|(2) Pix             |')
                print('|(3) Cartao          |')
                print('|====================|')

                forma_pagamento = int(input('Selecione o método de pagamento: '))
                if forma_pagamento > 0 and forma_pagamento < 4:
                    forma_pagamento = tipo_pagamento(forma_pagamento)
                    vendas.append(registrar_venda(valor, quant_tiquet, forma_pagamento, tipo_usuario))


def valor_usuario(tipo_usuario: int) -> int:

    if tipo_usuario == 1 or 2:
        valor = 5
    elif tipo_usuario == 3 or 4:
        valor = 10
    else:
        valor = 19
    return valor

def tipo_usuario(tipo_usuario: int) -> Usuarios:
    if tipo_usuario == 1:
        tipo_usuario = Usuarios.ALUNO
    elif tipo_usuario == 2:
        tipo_usuario = Usuarios.SERVIDOR_ATE3
    elif tipo_usuario == 3:
        tipo_usuario = Usuarios.SERVIDOR_ATE3
    elif tipo_usuario == 4:
        tipo_usuario = Usuarios.DOCENTE
    elif tipo_usuario == 5:
        tipo_usuario = Usuarios.EXTERNO
    return tipo_usuario

def tipo_pagamento(forma_pagamento) -> Pagamento:
    if forma_pagamento == 1:
        forma_pagamento = Pagamento.DINHEIRO
    elif forma_pagamento == 2:
        forma_pagamento = Pagamento.PIX
    elif forma_pagamento == 3:
        forma_pagamento = Pagamento.CARTAO
    return forma_pagamento

def registrar_venda(valor: int, quant_tiquet: int, forma_pagamento: Pagamento, tipo_usuario: Usuarios) -> Venda:
    Venda.pagamento = forma_pagamento
    Venda.usuario = tipo_usuario
    Venda.quantidade
    return Venda

if __name__ == '__main__':
    main()

'''
for i in vendas:
    Venda.usuario[i]
    Venda.usuario[0]
    Venda.pagamento[0]

    ou 
    
    vendas.usuario[i]
    vendas.usuario[0]
    vendas.pagamento[0]
    vendas.usuario[3]
'''