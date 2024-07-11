'''
13) Projete uma enumeração para representar a situação de um elevador que pode estar parado, subindo
ou descendo. Em seguida,

a) Sabendo que um elevador está parado e irá atender imediatamente uma solicitação, projete uma
função que determine, a partir do andar atual e do andar solicitado, qual será a situação do
elevador imediatamente após receber a solicitação.

b) Sabendo que um elevador só pode começar a se movimentar se estiver parado, projete uma função
que verifique se o elevador pode passar de um estado para outro.

'''

from enum import Enum, auto




class Posicao(Enum):
  PARADO = auto()
  SUBINDO = auto()
  DESCENDO = auto()




def subir_ou_descer(andarAtual: int, andarSolicitado: int) -> Posicao:
  '''
  Retorna se o elevador está subindo ou descendo de acordo com o *andarAtual* e o *andarSolicitado*
   >>> subir_ou_descer(1,5).name
  'SUBINDO'
  >>> subir_ou_descer(5,5).name
  'PARADO'
  >>> subir_ou_descer(6,3).name
  'DESCENDO'
  '''
  if andarAtual < andarSolicitado:
      posicao = Posicao.SUBINDO
  elif andarAtual > andarSolicitado:
      posicao = Posicao.DESCENDO
  else:
      posicao = Posicao.PARADO
  return posicao


def parado_movimento(estado_atual: Posicao) -> str:
   '''
  


   >>> parado_movimento(Posicao.PARADO)
   'O elevador pode começar a se movimentar'
   >>> parado_movimento(Posicao.SUBINDO)
   'O elevador já está se movimentando'
   >>> parado_movimento(Posicao.DESCENDO)
   'O elevador já está se movimentando'
   '''
   if estado_atual == Posicao.PARADO:
       situacao = 'O elevador pode começar a se movimentar'
   else:
       situacao = 'O elevador já está se movimentando'
   return situacao
