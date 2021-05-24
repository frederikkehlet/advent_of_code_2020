input = open('input.txt', 'r')
lines = input.readlines()

def solve():
    numbers = {}
    startingNumbers = [int(num) for num in list(lines[0].split(','))]

    for i in range(len(startingNumbers)):
        numbers[startingNumbers[i]] = i+1

    n = 0
    t = 7

    while t <= 2020:
        if n in numbers:
            diff = t - numbers[n]
            numbers[n] = t
            n = diff
            t += 1
        else:
            numbers[n] = t
            n = 0
            t += 1

    sortedNumbers = dict(sorted(numbers.items(), key = lambda x:x[1]))
    return list(sortedNumbers.items())[-1][0]

answer = solve()
print(answer)