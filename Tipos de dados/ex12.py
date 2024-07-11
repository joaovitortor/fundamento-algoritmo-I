from enum import Enum, auto


class Direcao(Enum):
   NORTE = auto()
   SUL = auto()
   LESTE = auto()
   OESTE = auto()


def direcao_oposta(direcao: Direcao) -> Direcao:
   '''
   Retorna a direção contrária a *direcao*


   >>> direcao_oposta(Direcao.NORTE).name
   'SUL'
   >>> direcao_oposta(Direcao.SUL).name
   'NORTE'
   >>> direcao_oposta(Direcao.OESTE).name
   'LESTE'
   >>> direcao_oposta(Direcao.LESTE).name
   'OESTE'
   '''
   if direcao == Direcao.NORTE:
       oposta = Direcao.SUL
   elif direcao == Direcao.SUL:
       oposta = Direcao.NORTE
   elif direcao == Direcao.LESTE:
       oposta = Direcao.OESTE
   else:
       oposta = Direcao.LESTE
   return oposta


def direcao_90_grausH(direcao: Direcao) -> Direcao:
   '''
   Retorna a direção 90 graus no sentido horario da *direcao*


   >>> direcao_90_grausH(Direcao.NORTE).name
   'LESTE'
   >>> direcao_90_grausH(Direcao.SUL).name
   'OESTE'
   >>> direcao_90_grausH(Direcao.OESTE).name
   'NORTE'
   >>> direcao_90_grausH(Direcao.LESTE).name
   'SUL'
   '''
   if direcao == Direcao.NORTE:
       direcao_horario = Direcao.LESTE
   elif direcao == Direcao.LESTE:
       direcao_horario = Direcao.SUL
   elif direcao == Direcao.SUL:
       direcao_horario = Direcao.OESTE
   else:
       direcao_horario = Direcao.NORTE
   return direcao_horario


def direcao_90_grausAH(direcao: Direcao) -> Direcao:
   '''
   Retorna a direção 90 graus no sentido anti-horario *direcao*


   >>> direcao_90_grausAH(Direcao.NORTE).name
   'OESTE'
   >>> direcao_90_grausAH(Direcao.SUL).name
   'LESTE'
   >>> direcao_90_grausAH(Direcao.OESTE).name
   'SUL'
   >>> direcao_90_grausAH(Direcao.LESTE).name
   'NORTE'
   '''
   return direcao_90_grausH(direcao_90_grausH(direcao_90_grausH(direcao)))


def quantos_graus(direcaoA: Direcao, direcaoB: Direcao) -> int:
   '''
   Calcula quantos graus tem entre *direcaoA* e *direcaoB*


   >>> quantos_graus(Direcao.NORTE, Direcao.SUL)
   180
   >>> quantos_graus(Direcao.SUL, Direcao.LESTE)
   270
   >>> quantos_graus(Direcao.OESTE, Direcao.OESTE)
   0
   >>> quantos_graus(Direcao.NORTE, Direcao.LESTE)
   90
   '''
   if direcaoB == direcao_90_grausH(direcaoA):
       graus = 90
   elif direcaoB == direcao_90_grausH(direcao_90_grausH(direcaoA)):
       graus = 180
   elif direcaoB == direcao_90_grausH(direcao_90_grausH(direcao_90_grausH(direcaoA))):
       graus = 270
   else:
       graus = 0
   return graus
