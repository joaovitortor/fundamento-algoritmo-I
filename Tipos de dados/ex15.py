'''
15) Projete uma estrutura para representar resoluções (largura e altura em pixels) de telas e imagens. Em
seguida,

a) Projete uma função que determine quantos mega pixels uma imagem tem dada a sua resolução.
O número de megapixel pode ser caculado multiplicando-se a altura e largura e dividindo-se por
1 milhão.

b) Projete uma função que indique se uma resolução tem aspecto (razão entre largura e altura)
de 4:3, 16:9 ou outro (projete um tipo enumerado para representar o aspecto). Por exemplo, a
resolução 1920 × 1080 tem aspecto 16:9, pois 1920 × 9 = 1080 × 16.

c) Projete uma função que receba duas resoluções, uma de uma imagem e outra de uma tela, e
verifique se a imagem pode ser exibida completamente na tela sem a necessidade de rotação ou
mudança de tamanho.

'''

from dataclasses import dataclass
from enum import Enum, auto


@dataclass
class Pixels:
   '''
  
   '''
   largura: int
   altura: int


class Aspecto(Enum):
   A1X1 = auto()
   A3X4 = auto()
   A4X3 = auto()
   A9X16 = auto()
   A16X9 = auto()
   NAO_CADASTRADA = auto()   




def quant_megapixels(resolucao: Pixels) -> float:
   '''

   >>> quant_megapixels(Pixels(1920,1080))
   2.0736
   >>> quant_megapixels(Pixels(1280,720))
   0.9216
   >>> quant_megapixels(Pixels(7680,4320))
   33.1776
   '''
   return resolucao.altura * resolucao.largura / 1000000


def aspecto_resolucao(resolucao: Pixels) -> Aspecto:
   if resolucao.largura == resolucao.altura:
       aspecto = Aspecto.A1X1
   elif resolucao.largura * 3 == resolucao.altura * 4:
       aspecto = Aspecto.A3X4
   elif resolucao.largura * 4 == resolucao.altura * 3:
       aspecto = Aspecto.A4X3
   elif resolucao.largura * 9 == resolucao.altura * 16:
       aspecto = Aspecto.A9X16
   elif resolucao.largura * 16 == resolucao.altura * 9:
       aspecto = Aspecto.A16X9
   else:
       aspecto = Aspecto.NAO_CADASTRADA
   return aspecto
