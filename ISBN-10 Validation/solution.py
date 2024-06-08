def valid_ISBN10(isbn): 
    if len(isbn) != 10:
        return False
    total = 0
    for idi, i in enumerate(isbn, start=1):
        if idi == 10 and i == "X":
            i = 10
        elif not i.isnumeric():
            return False
        total += idi * int(i)
    return total % 11 == 0