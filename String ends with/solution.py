def solution(text, ending):
    print(text)
    print(ending)
    print(text[-len(ending):])
    return text[-len(ending):] == ending