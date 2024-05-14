def strip_comments(strng, markers):
    first = True
    result = ""
    for strpart in strng.split("\n"):
        for mark in markers:
            strpart = strpart.split(mark)[0].rstrip()
        if first:
            first=False
        else:
            result += "\n"
        result += strpart
    return result