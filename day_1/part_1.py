# convert txt list to int list
input = open('input.txt', 'r')
numbers = input.readlines()

for i in range(len(numbers)): 
    numbers[i] = int(numbers[i].strip())

def solve():
    for first in numbers:        
        for second in numbers:
            if first + second == 2020:
                output = first * second
                return output

output = solve()
print(output)


