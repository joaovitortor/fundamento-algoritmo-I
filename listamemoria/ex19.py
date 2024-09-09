def adiciona_exclamacao(palavra: str, n: int) -> str:
    '''
    
    >>> adiciona_exclamacao('gol', 4)
    'gol!!!!'
    '''
    if n == 0:
        pal_exc = palavra
    else:
        pal_exc = adiciona_exclamacao(palavra, n-1) + '!'

    return pal_exc