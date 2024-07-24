from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Usuarios:
    '''
    Representa o ********. 
    **, ** e ** devem ser tal coisa. * e * devem ser menores que 60.
    '''
    #quantidade de alunos e quant de tiquet
    aluno: int
    #quantidade de servidores que ganham até 3 salarios minimos
    servidor_ate3: int
    #quantidade de servidores que ganham mais que 3 salarios minimos
    servidor_maior3: int
    #quantidade de docentes
    docente: int
    #quantidade de pessoas da comunidade externa
    externo: int

@dataclass
class Tiquet:
    '''
    Representa o ********. 
    **, ** e ** devem ser tal coisa. * e * devem ser menores que 60.
    '''
    #quantidade de tiquet por aluno
    aluno: int
    #quantidade de tiquet por servidores que ganham até 3 salarios minimos
    servidor_ate3: int
    #quantidade de tiquet por servidores que ganham mais que 3 salarios minimos
    servidor_maior3: int
    #quantidade de tiquet por docentes
    docente: int
    #quantidade de tiquet por pessoas da comunidade externa
    externo: int

class Receita_pagamento:
    '''
    
    '''
    dinheiro: int
    pix: int
    cartao: int

class Pagamento(Enum):
    '''O tipo do pagamento na venda'''
    DINHEIRO = auto()
    PIX = auto()
    CARTAO = auto()

def main():
    operacao = 0
    Usuarios.aluno = 0
    Tiquet.aluno = 0
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
            print('| (4) Servidor>3    |')
            print('| (5) Docentes      |')
            print('| (6) Externo       |')
            print('| (7) Cancelar      |')
            print('=====================')
            tipo_usuario = int(input('Escolha o usuario desejado inserindo o número: '))

            if tipo_usuario > 0 and tipo_usuario < 7:

                valor = valor_usuario(tipo_usuario)

                quant_tiquet = int(input('Quantos tiquetes estão sendo comprados? '))

                print('|====================|')
                print('| Forma de pagamento |')
                print('|(1) Dinheiro        |')
                print('|(2) Pix             |')
                print('|(3) Cartao          |')
                print('|====================|')

                forma_pagamento = int(input('Selecione o método de pagamento: '))

                print(registrar_venda(valor, quant_tiquet, forma_pagamento, tipo_usuario))


def valor_usuario(tipo_usuario: int) -> int:

    if tipo_usuario == 1 or 2:
        valor = 5
    elif tipo_usuario == 3 or 4:
        valor = 10
    else:
        valor = 19
    return valor

def registrar_venda(valor: int, quant_tiquet: int, forma_pagamento: int, tipo_usuario: int) -> str:
    
    if tipo_usuario == 1:
        Usuarios.aluno = Usuarios.aluno + 1
        Tiquet.aluno = Tiquet.aluno + 1
        text = 'Venda realizada para: Aluno / Quantidade de tiquet:', quant_tiquet, '/valor:', valor * quant_tiquet, '/ forma pagamento:', forma_pagamento

    return text

if __name__ == '__main__':
    main()
