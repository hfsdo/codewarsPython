def solution(array_a, array_b):
    total = 0
    for ida, a in enumerate(array_a):
        total += abs(a - array_b[ida]) ** 2
    ida+=1
    return total/ida
