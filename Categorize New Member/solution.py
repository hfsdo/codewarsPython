def open_or_senior(data):
    result = []
    for member in data:
        if member[0] >= 55 and member[1] > 7:
            result += ["Senior"]
        else:
            result += ["Open"]
    return result