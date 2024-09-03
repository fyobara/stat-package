def median(n):
    try:
        if len(n) % 2:
            return sorted(n)[len(n) // 2]
        else:
            return (sorted(n)[(len(n)-1) // 2] + sorted(n)[(len(n)+1) // 2]) / 2
    except ZeroDivisionError:
        return 'A lista não deve estar vazia!'