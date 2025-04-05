def filter_list(l):
    result = []
    for i in l:
        if isinstance(i, int):
            result.append(i)
    return result