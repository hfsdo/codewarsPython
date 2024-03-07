def descending_order(num):
    numLst = list(str(num))
    numLst.sort(reverse=True)
    return int("".join(numLst))