def two_sum(numbers, target):
    for i in numbers:
        rest = target - i
        if rest in numbers[numbers.index(i)+1:len(numbers)]:
            return (numbers.index(i),numbers.index(rest, numbers.index(i)+1))