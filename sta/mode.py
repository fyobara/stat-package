def mode(n):
    try:

        lista = []

        for i in n:
            if i not in lista:
                lista.append(n.count(i))

        if lista.count(max(lista)) > max(lista):
            return f'Amodal'
        else:
            return n[lista.index(max(lista))]

    except IndexError:
        return 'A lista não deve estar vazia!'