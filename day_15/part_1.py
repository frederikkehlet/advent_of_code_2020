input = open('input.txt', 'r')
lines = input.readlines()

def solve():
    numbers = [int(num) for num in list(reversed(lines[0].split(',')))]
    turn = len(numbers) + 1
    while turn <= 2020:
        lastSpokenNumber = numbers[0]
        previousNumbers = numbers[1:]
        
        i = 0
        latestTurn = 0
        spokenPreviously = False
        while i < len(previousNumbers):        
            if lastSpokenNumber == int(previousNumbers[i]):
                spokenPreviously = True
                latestTurn = i
                break
            i += 1
        
        if not spokenPreviously: numbers.insert(0,0)
        else: numbers.insert(0,latestTurn + 1)
        turn += 1
        
    return numbers[0]

answer = solve()
print(answer)