def mean(n):
    try:
        return sum(n) / len(n)
    except ZeroDivisionError:
        return 'A lista não deve estar vazia!'