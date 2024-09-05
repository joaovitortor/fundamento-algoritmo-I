from dataclasses import dataclass
from enum import Enum, auto
import math

class Usuarios(Enum):
    '''
    O tipo de usuario que pode realizar a venda.
    '''
    ALUNO = auto()
    SERVIDOR_ATE3 = auto()
    SERVIDOR_MAIOR3 = auto()
    DOCENTE = auto()
    EXTERNO = auto()

class Pagamento(Enum):
    '''
    O tipo do pagamento na venda
    '''
    DINHEIRO = auto()
    PIX = auto()
    CARTAO = auto()

@dataclass
class Venda:
    '''
    Representa cada venda realizada.
    quantidade deve ser um número positivo.
    '''
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

                total = quant_tiquet * valor_usuario(tipo_usuario(escolha_usuario))

                print('TOTAL: R$', total)

                print('|====================|')
                print('| Forma de pagamento |')
                print('|(1) Dinheiro        |')
                print('|(2) Pix             |')
                print('|(3) Cartao          |')
                print('|====================|')

                forma_pagamento = int(input('Selecione o método de pagamento: '))

                if forma_pagamento > 0 and forma_pagamento < 4:

                    confirmar = str(input('Confirmar venda? [s/n]'))

                    if confirmar == 's' or confirmar == 'S':

                        vendas.append(Venda(tipo_usuario(escolha_usuario), tipo_pagamento(forma_pagamento), quant_tiquet))

                        
                        print('===========================')
                        print('Venda realizada com sucesso')
                        print('Usuario:', tipo_usuario(escolha_usuario).name)
                        print('Quantidade de tiquet:', quant_tiquet)
                        print('Total:', total)
                        print('===========================')

        elif operacao == 2:
            if vendas != []:
                print('Alunos:     ', grafico_usuario(vendas, Usuarios.ALUNO))
                print('Servidor<3: ', grafico_usuario(vendas, Usuarios.SERVIDOR_ATE3))
                print('Servidor>3: ', grafico_usuario(vendas, Usuarios.SERVIDOR_MAIOR3))
                print('Docente:    ', grafico_usuario(vendas, Usuarios.DOCENTE))
                print('Externo:    ', grafico_usuario(vendas, Usuarios.EXTERNO))            

                for i in range(quantidade_linhas_receita(vendas), -1, -1):
                    print('    ' + grafico_receita(vendas, Pagamento.CARTAO)[i] + '      ' + grafico_receita(vendas, Pagamento.PIX)[i] + '       ' + grafico_receita(vendas, Pagamento.DINHEIRO)[i])
                print('|  CARTAO  |    PIX    | DINHEIRO |')
            else:
                print('Por favor, realizar pelo menos uma venda para solicitar os relatórios')


def valor_usuario(tipo_usuario: Usuarios) -> int:
    '''
    Retorna o valor do tiquet do usuario selecionado pelo *tipo_usuario*

    >>> valor_usuario(Usuarios.ALUNO)
    5
    >>> valor_usuario(Usuarios.SERVIDOR_ATE3)
    5
    >>> valor_usuario(Usuarios.SERVIDOR_MAIOR3)
    10
    >>> valor_usuario(Usuarios.DOCENTE)
    10
    >>> valor_usuario(Usuarios.EXTERNO)
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
    Analisa qual elemento da classe enumerada Usuarios foi selecionado pela *escolha_usuario*
    
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

def tipo_pagamento(forma_pagamento: int) -> Pagamento:
    '''
    Analisa qual elemento da classe enumerada Pagamentos foi selecionado pela *forma_pagamento*
    
    Exemplos
    >>> tipo_pagamento(1).name
    'DINHEIRO'
    >>> tipo_pagamento(2).name
    'PIX'
    >>> tipo_pagamento(3).name
    'CARTAO'
    '''
    if forma_pagamento == 1:
        pagamento = Pagamento.DINHEIRO
    elif forma_pagamento == 2:
        pagamento = Pagamento.PIX
    elif forma_pagamento == 3:
        pagamento = Pagamento.CARTAO
    return pagamento

def contar_usuario(vendas: list[Venda], usuario: Usuarios) -> int:
    '''
    Realiza a contagem de quantas vezes um tipo de usuario está armazenado na lista *vendas*

    Exemplos
    >>> contar_usuario([], Usuarios.ALUNO)
    0
    >>> contar_usuario([Venda(Usuarios.ALUNO, Pagamento.CARTAO, 3), 
    ... Venda(Usuarios.DOCENTE, Pagamento.PIX, 3)], 
    ... Usuarios.ALUNO)
    1
    '''

    quant_usuario = 0

    for Venda in vendas:
        if Venda.usuario == usuario:
            quant_usuario = quant_usuario + 1
    return quant_usuario

def contar_pagamento(vendas: list[Venda], pagamento: Pagamento) -> int:
    '''
    Computa a receita de uma forma de pagamento, *pagamento*, realizada em toda as *vendas*
    
    Exemplos
    >>> contar_pagamento([], Pagamento.CARTAO)
    0
    >>> contar_pagamento([Venda(Usuarios.ALUNO, Pagamento.CARTAO, 3), 
    ... Venda(Usuarios.DOCENTE, Pagamento.CARTAO, 3)], 
    ... Pagamento.CARTAO)
    45
    '''
    quant_pagamento = 0
    for Venda in vendas:
        if Venda.pagamento == pagamento:
            quant_pagamento = quant_pagamento + Venda.quantidade * valor_usuario(Venda.usuario)
    return quant_pagamento

def maior(a: int, b: int) -> int:
    '''
    Verifica se *a* é maior que *b* ou se *b* é maior que *a*

    Exemplos
    >>> maior(10,11)
    11
    >>> maior(5,5)
    5
    >>> maior(12,5)
    12
    '''
    if a >= b:
        maior = a
    else:
        maior = b
    return maior

def verificar_maior(vendas: list[Venda]) -> int:
    '''
    Verifica qual tipo de usuario que mais comprou tiquets em toda a lista *vendas* e computa quantas vezes esse tipo de usuario realizou uma venda
    
    Exemplos
    >>> verificar_maior([Venda(Usuarios.ALUNO, Pagamento.CARTAO, 3),
    ... Venda(Usuarios.DOCENTE, Pagamento.PIX, 3),
    ... Venda(Usuarios.ALUNO, Pagamento.CARTAO, 2)])
    2
    '''
    maior_quantidade = maior(contar_usuario(vendas, Usuarios.ALUNO), maior(contar_usuario(vendas, Usuarios.SERVIDOR_ATE3), maior(contar_usuario(vendas, Usuarios.SERVIDOR_MAIOR3), maior(contar_usuario(vendas, Usuarios.DOCENTE), contar_usuario(vendas, Usuarios.EXTERNO)))))
    return maior_quantidade

def grafico_usuario(vendas: list[Venda], usuario: Usuarios) -> str:
    '''
    Cria um gráfico visual da porcentagem de tipo de *usuario* presente na lista *vendas* comparado a todos os tipos de usuarios

    Exemplos
    >>> grafico_usuario([Venda(Usuarios.ALUNO, Pagamento.CARTAO, 3), 
    ... Venda(Usuarios.DOCENTE, Pagamento.PIX, 3)], 
    ... Usuarios.ALUNO)
    '[=================] 50.0%'
    >>> grafico_usuario([], Usuarios.ALUNO)
    ''
    '''

    linha_grafico = ''
    maior_quantidade = verificar_maior(vendas)

    total = len(vendas)

    if total != 0:
        porc = contar_usuario(vendas, usuario) / total * 100

        if porc < 3 and porc != 0:
            tamanho = '='
        else:
            tamanho = '=' * int(round(porc / 3))

        if porc < 10:
            linha_porcentagem = ' ' + str(round(porc, 2)) + '%'
        else:
            linha_porcentagem = '' + str(round(porc, 2)) + '%'

        if contar_usuario(vendas, usuario) != maior_quantidade:
            maior_porcentagem = maior_quantidade / total * 100
            espaco = str(' ' * int(round((maior_porcentagem - porc) / 3)))
        else:
            espaco = ''
        linha_grafico = '[' + tamanho + '] ' + espaco + linha_porcentagem

    return linha_grafico

def quantidade_linhas_receita(vendas: list[Venda]) -> int:
    '''
    Calcula qual é a maior linha do grafico da receita gerada por cada forma de pagamento da lista *vendas*

    Exemplos
    >>> quantidade_linhas_receita([Venda(Usuarios.ALUNO, Pagamento.CARTAO, 3), 
    ... Venda(Usuarios.DOCENTE, Pagamento.PIX, 3),
    ... Venda(Usuarios.ALUNO, Pagamento.DINHEIRO, 10)])
    4
    >>> quantidade_linhas_receita([])
    0
    '''

    total = contar_pagamento(vendas, Pagamento.CARTAO) + contar_pagamento(vendas, Pagamento.DINHEIRO) + contar_pagamento(vendas, Pagamento.PIX)

    if total != 0:
        maior_receita = maior(contar_pagamento(vendas, Pagamento.CARTAO), maior(contar_pagamento(vendas, Pagamento.DINHEIRO), contar_pagamento(vendas, Pagamento.PIX)))
        
        maior_porcentagem = maior_receita / total * 100
        total_linhas = math.ceil((maior_porcentagem / 3)/5)
    else:
        total_linhas = 0

    return total_linhas

def grafico_receita(vendas: list[Venda], pagamento: Pagamento) -> list[str]:
    '''
    Realiza o gráfico da porcentagem da receita obtida com cada forma de pagamento da lista *venda*.

    '''
    total = contar_pagamento(vendas, Pagamento.CARTAO) + contar_pagamento(vendas, Pagamento.DINHEIRO) + contar_pagamento(vendas, Pagamento.PIX)

    porcentagem = contar_pagamento(vendas, pagamento) / total * 100

    grafico: list[str] = []

    total_linhas = quantidade_linhas_receita(vendas)
    
    tamanho = math.ceil(porcentagem / 3)
    
    quantidade_linhas = math.ceil(tamanho/5)
    
    linhas_vazias = total_linhas - quantidade_linhas
    
    for i in range(0, quantidade_linhas):
        if i != quantidade_linhas - 1:
            grafico.append('\u2588\u2588\u2588\u2588\u2588')
        else:
            grafico.append('\u2588' * (tamanho - 5 * (quantidade_linhas - 1)) + ' ' * (5 - (tamanho - 5 * (quantidade_linhas - 1))))
    
    if total_linhas == quantidade_linhas:
        grafico.append(str(round(porcentagem, 1)) + '%')

    for i in range(0, linhas_vazias + 1):
        if i == 0:
            grafico.append(str(round(porcentagem, 1)) + '%')
        else:
            grafico.append('     ')

    return grafico

if __name__ == '__main__':
    main()
