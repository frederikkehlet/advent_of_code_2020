map = []

input = open('input.txt', 'r')
lines = input.readlines()

for i in range(len(lines)): 
    lines[i] = lines[i].strip()
    map.append(list(lines[i]))
    
def solve(slope_x, slope_y):
    n_trees = 0
    x = 0
    y = 0
    
    while y < len(map):
        if (map[y][x % len(map[0])] == '#'):
            n_trees += 1
        x += slope_x
        y += slope_y

    return n_trees

output = solve(1,1) * solve(5,1) * solve(7,1) * solve(1,2) * solve(3,1)
print(output)



