import sys
from dataclasses import dataclass
from enum import Enum, auto

class Genero(Enum):
    FEMININO = auto()
    MASCULINO = auto()
    EQUIPE_MISTA = auto()
    AMBOS = auto()

@dataclass
class Classificacao:
    nome: str
    ouro: int
    prata: int
    bronze: int
    feminino: bool
    masculino: bool

@dataclass
class Informacoes:
    nome: str
    medalha: str 
    genero: Genero

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])
    informacoes = (informacoes_tabela(tabela))
    paises = nome_paises(informacoes)
    alterar_valores(informacoes,paises)
    ordena_lista(paises)
    pais_generoF = listar_genero(paises, Genero.FEMININO)
    print(pais_generoF)
    pais_generoM = listar_genero(paises, Genero.MASCULINO)
    print(pais_generoF)
    print('País Ouro Prata Bronze Total')
    for i in paises:
        total = i.ouro + i.prata + i.bronze
        print(i.nome, formata_numero(i.ouro), formata_numero(i.prata), formata_numero(i.bronze), formata_numero(total))

    print('===============================')
    print('Masculino')
    print('País Ouro Prata Bronze Total')

    for i in pais_generoM:
        print(i.nome, formata_numero(i.ouro), formata_numero(i.prata), formata_numero(i.bronze), formata_numero(total))

    print('===============================')
    print('Feminino')
    print('País Ouro Prata Bronze Total')
    for j in pais_generoF:
        print(j.nome, formata_numero(j.ouro), formata_numero(j.prata), formata_numero(j.bronze), formata_numero(total))
                 
    # TODO: computar e exibir o quadro de medalhas
    # TODO: computar e exibir os países que tiverem apenas
    #       atletas de um único gênero premiados
    
 

def le_arquivo(nome: str) -> list[list[str]]:
    '''
    Lê o conteúdo do arquivo *nome* e devolve uma lista onde cada elemento é
    uma lista com os valores das colunas de uma linha (valores separados por
    vírgula). A primeira linha do arquivo, que deve conter o nome das
    colunas, é descartado.

    Por exemplo, se o conteúdo do arquivo for

    tipo,cor,ano
    carro,verde,2010
    moto,branca,1995

    a resposta produzida é
    [['carro', 'verde', '2010'], ['moto', 'branca', '1995']]
    '''
    try:
        with open(nome) as f:
            tabela = []
            linhas = f.readlines()
            for i in range(1, len(linhas)):
                tabela.append(linhas[i].split(','))
            return tabela
    except IOError as e:
        print(f'Erro na leitura do arquivo "{nome}": {e.errno} - {e.strerror}.');
        sys.exit(1)


def informacoes_tabela(tabela: list[list[str]]) -> list[Informacoes]:
    lista: list[Informacoes] = []
    for i in tabela:
        if i[5] == 'W':
            genero = Genero.FEMININO
        elif i[5] == 'M':
            genero = Genero.MASCULINO
        elif i[5] == 'X':
            genero = Genero.EQUIPE_MISTA
        else:
            genero = Genero.AMBOS
        lista.append(Informacoes(i[4], i[1], genero))
    return lista


def contar_medalha(informacoes: list[Informacoes], nome: str, medalha: str) -> int:
    '''
    Computa a quantidade de cada tipo de *medalha* de acordo com o *nome* do país na *tabela*

    >>>
    '''
    if informacoes == []:
        medalhas = 0
    else: 
        if nome == informacoes[0].nome and informacoes[0].medalha == medalha:
            medalhas = 1 + contar_medalha(informacoes[1:], nome, medalha)
        else:
            medalhas = contar_medalha(informacoes[1:], nome, medalha)
    return medalhas

def verifica_genero(informacoes: list[Informacoes], nome: str, genero: Genero, tem_genero = False) -> bool:
    if informacoes == []:
        tem_genero = False
    if informacoes != [] and not tem_genero:
        if informacoes[0].nome == nome and informacoes[0].genero == genero:
            tem_genero = True
        else:
            tem_genero = verifica_genero(informacoes[1:], nome, genero)
    return tem_genero

def listar_genero(paises: list[Classificacao], genero: Genero) -> list[Classificacao]:
    if paises == []:
        lista = []
    else:
        if genero == Genero.FEMININO:
            if paises[0].feminino and (not paises[0].masculino):
                lista = [paises[0]] + listar_genero(paises[1:], genero)
            else:
                listar_genero(paises[1:], genero)
        elif genero == Genero.MASCULINO:
            if paises[0].masculino and (not paises[0].feminino):
                lista = [paises[0]] + listar_genero(paises[1:], genero)
            else:
                listar_genero(paises[1:], genero)
        else:
            listar_genero(paises[1:], genero)
    return lista


def alterar_valores(informacoes: list[Informacoes], paises: list[Classificacao]) -> None:
    '''
    Altera os valores de cada elemento da classe Classificacao na lista *paises*, inserindo o valor
    total de medalhas de ouro, prata e broze e atualizando o feminino e masculino para True quando 
    houver e False quando não houver.


    '''
    for i in range(0, len(paises)):
        paises[i].ouro = contar_medalha(informacoes, paises[i].nome, '1')
        paises[i].prata = contar_medalha(informacoes, paises[i].nome, '2')
        paises[i].bronze = contar_medalha(informacoes, paises[i].nome, '3')
        paises[i].feminino = verifica_genero(informacoes, paises[i].nome, Genero.FEMININO)
        paises[i].masculino = verifica_genero(informacoes, paises[i].nome, Genero.MASCULINO)

def nome_paises(informacoes: list[Informacoes]) -> list[Classificacao]:
    pais: list[str] = []
    lista_nomes: list[Classificacao] = []
    for i in informacoes:
        nao_incluso = True
        for j in range(0, len(pais)):
            if i.nome == pais[j]:
                nao_incluso = False
        if nao_incluso:
            pais.append(i.nome)
    for k in pais:
        lista_nomes.append(Classificacao(k,0,0,0, False, False))
    return lista_nomes


def ordena_lista(paises: list[Classificacao], n: int = 0) -> None:
    '''
    Altera a lista *paises*, ordenando os países de acordo com os pesos das medalhas
   
    explicar peso medalha


    '''
    if n < len(paises):
        maior = paises[n]
        indice = n
        for i in range(n, len(paises)):
            if paises[i].ouro > maior.ouro:
                maior = paises[i]
                indice = i
            elif paises[i].ouro == maior.ouro:
                if paises[i].prata > maior.prata:
                    maior = paises[i]
                    indice = i
                elif paises[i].prata == maior.prata:
                    if paises[i].bronze > maior.bronze:
                        maior = paises[i]
                        indice = i
                    elif paises[i].nome < maior.nome:
                        maior = paises[i]
                        indice = i

        ordena_elementos(paises, indice, n)
        ordena_lista(paises, n+1)

def ordena_elementos(paises: list[Classificacao], indice, repeticao) -> None:

    i = len(paises[:indice])

    while i > repeticao:
        # troca lst[i] <-> lst[i - 1]
        t = paises[i]
        paises[i] = paises[i - 1]
        paises[i - 1] = t
        i = i - 1
        

def formata_numero(n: int) -> str:
    if n < 10:
        formatado = ('    ' + str(n))
    elif n > 99:
        formatado = ('  ' + str(n))
    else:
        formatado = ('   ' + str(n))

    return formatado

if __name__ == '__main__':
    import sys
    # define o limite de chamadas recursivas
    sys.setrecursionlimit(10000)
    main()


#verificar qual o maior e passar ele para a primeira posição, após isso verificar do [n:] e passar o maior para a n posição