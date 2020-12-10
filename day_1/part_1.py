# convert txt list to int list
input = open('input.txt', 'r')
numbers = input.readlines()

for i in range(len(numbers)): 
    numbers[i] = int(numbers[i].strip())

# create variable "comparer"
comparer = 0

def solve():
    for num in numbers:
        comparer = num
        for rest in numbers:
            if rest + comparer == 2020:
                output = rest * comparer
                return output

output = solve()
print(output)


