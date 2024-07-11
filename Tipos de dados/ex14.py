'''
14) Projete uma estrutura para representar uma data com dia, mês e ano. Em seguida,

a) Projete uma função que receba como entrada uma string que representa uma data no formato
“dd/mm/aaaa”, e converta a string para a data equivalente.

b) Projete uma função que verifique se uma data é o último dia do ano.

c) Projete uma função que receba duas datas e produza verdadeiro se a primeira vem antes que a
segunda.

d) (Desafio) Projete uma função que verifique se uma data é válida. Considere que em anos bissextos
fevereiro tem 29 dias e que um ano é bissexto se é múltiplo de 400 ou é múltiplo de 4 mas não é
múltiplo de 100.

'''
from dataclasses import dataclass


@dataclass
class Calendario:
   '''
   Representa as datas do calendário.
   horas, minutos e segundos devem ser positivos.
   '''
   dia: int
   mes: int
   ano: int


def converta_data(datastr: str) -> Calendario:
   '''
   
   >>> converta_data('06/01/2005')
   Calendario(dia=6, mes=1, ano=2005)
   >>> converta_data('25/06/2014')
   Calendario(dia=25, mes=6, ano=2014)
   >>> converta_data('25/11/1977')
   Calendario(dia=25, mes=11, ano=1977)
   '''
   diastr = int(datastr[:2])
   messtr = int(datastr[3:5])
   anostr = int(datastr[6:])
   data: Calendario = Calendario(diastr, messtr, anostr)
   return data


def ultimo_dia_ano(data: Calendario) -> bool:
   '''

   >>> ultimo_dia_ano(Calendario(31,12,2005))
   True
   >>> ultimo_dia_ano(Calendario(31,11,2010))
   False
   >>> ultimo_dia_ano(Calendario(30,12,2000))
   False
   '''
   return data.mes == 12 and data.dia == 31


def data_antes_depois(dataA: Calendario, dataB: Calendario) -> bool:
   '''

   >>> data_antes_depois(Calendario(6, 1, 2005), Calendario(25, 6, 2014))
   True
   >>> data_antes_depois(Calendario(1, 5, 2005), Calendario(25, 6, 2005))
   True
   >>> data_antes_depois(Calendario(1, 5, 2005), Calendario(25, 5, 2005))
   True
   >>> data_antes_depois(Calendario(25, 5, 2005), Calendario(1, 5, 2005))
   False
   '''
   if dataA.ano < dataB.ano:
       dataAD = True
   elif dataA.ano == dataB.ano and dataA.mes < dataB.mes:
       dataAD = True
   elif dataA.ano == dataB.ano and dataA.mes == dataB.mes and dataA.dia < dataB.dia:
       dataAD = True
   else:
       dataAD = False
   return dataAD


def data_valida(data: Calendario) -> bool:


   '''

   >>> data_valida(Calendario(29,2,2024))
   True
   >>> data_valida(Calendario(29,2,2023))
   False
   >>> data_valida(Calendario(29,2,2023))
   False
   >>> data_valida(Calendario(31,4,2022))
   False
   >>> data_valida(Calendario(31,5,2022))
   True
   '''
   valida = False
   if data.mes <= 12:
       if data.mes % 2 != 0 or data.mes == 10:
           if data.dia > 0 and data.dia <= 31:
               valida = True
       elif (data.mes == 2 and data.ano % 400 == 0) or \
               (data.ano % 4 == 0 and data.ano % 100 != 0):
           if data.dia > 0 and data.dia <= 29:
               valida = True
       elif (data.mes == 2 and not((data.ano % 400 == 0)) or \
               (data.ano % 4 == 0 and data.ano % 100 != 0)):
           if data.dia > 0 and data.dia <= 28:
               valida = True
       elif data.mes % 2 == 0:
           if data.dia > 0 and data.dia <= 30:
               valida = True
   return valida
