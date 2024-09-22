def square_digits(num):
    numstr = str(num)
    resstr = ''
    for i in range(len(numstr)):
        resstr += str(int(numstr[i])**2)
    return int(resstr)
    