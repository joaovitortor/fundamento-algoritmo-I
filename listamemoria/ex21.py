def remove_branco_nulo(lst: list[int]) -> None:
    '''

    >>> lst = [1,0,3,4,0,5,0,1]
    >>> remove_branco_nulo(lst)
    >>> print(lst)
    [3, 4, 5]
    '''
    for i in range(len(lst)-1,-1,-1):
        if lst[i] == 0 or lst[i] == 1:
            t = lst[len(lst)-1]
            lst[len(lst)-1] = lst[i]
            lst[i] = t
            lst.pop()