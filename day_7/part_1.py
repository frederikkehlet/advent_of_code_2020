with open('input.txt', 'r') as f:
    lines = f.readlines()

dictionary = {}

for line in lines:
     line_split = line.split('contain')
     dictionary[line_split[0].strip()] = line_split[1].strip().split(', ')


print(dictionary['wavy green bags'])

bags = []

def solve(bag, bags):

solve('wavy green bags', bags)

print(len(bags))

