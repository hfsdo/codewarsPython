def get_sum(a,b):
    if a == b:
        return a
    elif a < b:
        step = 1
    else:
        step = -1
    result = b
    for i in range(a, b, step):
        result += i
    return result