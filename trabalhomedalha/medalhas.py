import sys
from dataclasses import dataclass

@dataclass
class Pais:
    nome: str
    ouro: int
    prata: int
    bronze: int
    feminino: bool
    masculino: bool

def main():
    if len(sys.argv) < 2:
        print('Nenhum nome de arquivo informado.')
        sys.exit(1)

    if len(sys.argv) > 2:
        print('Muitos parâmetro. Informe apenas um nome de arquivo.')
        sys.exit(1)

    tabela = le_arquivo(sys.argv[1])
    
    paises = nome_paises(tabela)
    contar_medalhas(tabela,paises)
    verifica_maior(paises)
    grafico = grafico_medalha(paises)

    print(grafico[1])
    for i in grafico:
        print(i[0], i[1], i[2], i[3])

    print('===============================')
    print('Masculino')
    print(grafico[0][0],grafico[0][1],grafico[0][2],grafico[0][3])
    for i in grafico[1:]:
        if i[5] == 'True' and i[4] == 'False':
            print(i[0], i[1], i[2], i[3])

    print('===============================')
    print('Feminino')
    print(grafico[0][0],grafico[0][1],grafico[0][2],grafico[0][3])
    for i in grafico[1:]:
        if i[4] == 'True' and i[5] == 'False':
            print(i[0], i[1], i[2], i[3])
                 

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

def contar_ouro(tabela: list[list[str]], nome) -> int:

    if tabela == []:
        ouro = 0
    else: 
        if nome == tabela[0][4] and tabela[0][1] == '1':
            ouro = 1 + contar_ouro(tabela[1:], nome)
        else:
            ouro = contar_ouro(tabela[1:], nome)
    return ouro

def contar_prata(tabela: list[list[str]], nome) -> int:

    if tabela == []:
        prata = 0
    else: 
        if nome == tabela[0][4] and tabela[0][1] == '2':
            prata = 1 + contar_prata(tabela[1:], nome)
        else:
            prata = contar_prata(tabela[1:], nome)
    return prata

def contar_bronze(tabela: list[list[str]], nome) -> int:

    if tabela == []:
        bronze = 0
    else: 
        if nome == tabela[0][4] and tabela[0][1] == '3':
            bronze = 1 + contar_bronze(tabela[1:], nome)
        else:
            bronze = contar_bronze(tabela[1:], nome)
    return bronze

def contar_feminino(tabela: list[list[str]], nome) -> bool:
    tem_f = False
    i = 0
    while (not tem_f) and i < len(tabela):
        if tabela[i][4] == nome and tabela[i][5] == 'W':
            tem_f = True
        i = i+1
    return tem_f

def contar_masculino(tabela: list[list[str]], nome) -> bool:
    tem_m = False
    i = 0
    while (not tem_m) and i < len(tabela):
        if tabela[i][4] == nome and tabela[i][5] == 'M':
            tem_m = True
        i = i+1
    return tem_m

def contar_medalhas(tabela: list[list[str]], paises: list[Pais]) -> None:
    for i in range(0, len(paises)):
        paises[i].ouro = contar_ouro(tabela, paises[i].nome)
        paises[i].prata = contar_prata(tabela, paises[i].nome)
        paises[i].bronze = contar_bronze(tabela, paises[i].nome)
        paises[i].feminino = contar_feminino(tabela, paises[i].nome)
        paises[i].masculino = contar_masculino(tabela, paises[i].nome)

def nome_paises(tabela: list[list[str]]) -> list[Pais]:
    pais: list[str] = []
    lista_nomes: list[Pais] = []
    for i in tabela:
        nao_incluso = True
        for j in range(0, len(pais)):
            if i[4] == pais[j]:
                nao_incluso = False
        if nao_incluso:
            pais.append(i[4])
    for k in pais:
        lista_nomes.append(Pais(k,0,0,0, False, False))
    return lista_nomes


def verifica_maior(paises: list[Pais], n: int = 0) -> None:
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

        ordena_lista(paises, indice, n)
        n = n+1
        verifica_maior(paises, n)

def ordena_lista(paises: list[Pais], indice, repeticao) -> None:

    i = len(paises[:indice])

    while i > repeticao:
        # troca lst[i] <-> lst[i - 1]
        t = paises[i]
        paises[i] = paises[i - 1]
        paises[i - 1] = t
        i = i - 1
        
def grafico_medalha(paises: list[Pais]) -> list[list[str]]:
    grafico: list[list[str]] = []
    linha: list[str] = []
    linha = ['País', 'Ouro', 'Prata', 'Bronze','','']
    grafico.append(linha)
    for i in paises:
        linha = [str(i.nome),('   ' + formata_numero(i.ouro)), ('   ' + formata_numero(i.prata)),('   ' + formata_numero(i.bronze)), (str(i.feminino)), (str(i.masculino))]
        grafico.append(linha)
    return grafico

def formata_numero(n: int) -> str:
    if n < 10:
        formatado = (' ' + str(n))
    elif n > 9:
        formatado = str(n)
    return formatado

if __name__ == '__main__':
    import sys
    # define o limite de chamadas recursivas
    sys.setrecursionlimit(10000)
    main()


#verificar qual o maior e passar ele para a primeira posição, após isso verificar do [n:] e passar o maior para a n posição
