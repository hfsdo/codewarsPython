def friend(x):
    print(x)
    result = []
    for name in x:
        if len(name) == 4:
            result.append(name)
    return result