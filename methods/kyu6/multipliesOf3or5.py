def solution(number):
    count = 0
    if number <= 0:
        return count
    for i in range(1, number):
        if i % 3 == 0 or i % 5 == 0:
            count += i

    return count
