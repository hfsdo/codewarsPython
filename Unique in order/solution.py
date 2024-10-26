def unique_in_order(sequence):
    cur = ''
    result = []
    for s in sequence:
        if s != cur:
            result.append(s)
            cur = s
    return result