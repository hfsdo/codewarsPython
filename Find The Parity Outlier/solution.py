def find_outlier(integers):
    isOdd = 0
    for i in range(3):
        isOdd += integers[i]%2
    print(isOdd)
    if isOdd >= 2:
        isOdd = 1
    else:
        isOdd = 0
    
    for i in integers:
        if i%2 != isOdd:
            return i