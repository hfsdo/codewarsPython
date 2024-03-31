def parse(data):
    result = []
    val = 0
    for c in data:
        if c == 'i':
            val += 1
        elif c == 'd':
            val -= 1
        elif c == 's':
            val *= val
        elif c == 'o':
            result.append(val)
    return result