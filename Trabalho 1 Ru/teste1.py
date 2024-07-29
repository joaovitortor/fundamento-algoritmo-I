from dataclasses import dataclass
from enum import Enum, auto

@dataclass
class Usuarios:
    '''
    Representa o ********. 
    **, ** e ** devem ser tal coisa. * e * devem ser menores que 60.
    '''
    #quantidade de alunos
    alunos: int
    #quantidade de servidores que ganham até 3 salarios minimos
    servidores_ate3: int
    #quantidade de servidores que ganham mais que 3 salarios minimos
    servidores_maior3: int
    #quantidade de docentes
    docentes: int
    #quantidade de pessoas da comunidade externa
    externo: int

class Pagamento(Enum):
    '''O tipo do pagamento na venda'''
    DINHEIRO = auto()
    PIX = auto()
    CARTAO = auto()

def main():
    opracao = 0
    while operacao != 3:
        print('========================')
        print('|     OPERAÇÕES        |')
        print('| (1) Registrar venda  |')
        print('| (2) Exibir relatório |')
        print('| (3) Encerrar         |')
        print('========================')
        operacao = int(input('Escolha a opção desejada inserindo o número: '))

        if operacao == 1:
            
def selecionar_usuario(operacao: int) -> int:
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
        
def registrar_venda(tipo_usuario: int) -> str:

if __name__ == '__main__':
    main()
