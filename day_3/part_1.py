map = []

input = open('input.txt', 'r')
lines = input.readlines()

for i in range(len(lines)): 
    lines[i] = lines[i].strip()
    map.append(list(lines[i]))
    
def solve(x, y):
    n_trees = 0
    
    while y < len(map):
        if (map[y][(x * y) % len(map[y])] == '#'):
            n_trees += 1
        y += 1

    return n_trees

output = solve(3,1)
print(output)



