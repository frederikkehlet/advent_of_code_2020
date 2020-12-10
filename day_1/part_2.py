# convert txt list to int list
input = open('input.txt', 'r')
numbers = input.readlines()

for i in range(len(numbers)): 
    numbers[i] = int(numbers[i].strip())

def solve():
    for first in numbers:        
        for second in numbers:
            for third in numbers:
                if first + second + third == 2020:
                    output = first * second * third
                    return output

output = solve()
print(output)


