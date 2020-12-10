input = open('input.txt', 'r')
lines = input.readlines()

for i in range(len(lines)): 
    lines[i] = lines[i].strip()

def solve():
    n_valid = 0

    for line in lines:
        split = line.split(': ')
        policy = split[0]
        pwd = split[1]
        policy_split = policy.split(' ')
        positions = policy_split[0].split('-')
        char = policy_split[1]

        pos_1 = int(positions[0]) - 1 # account for index start 0
        pos_2 = int(positions[1]) - 1 # account for index start 0

        if((pwd[pos_1] == char) != (pwd[pos_2] == char)): # XOR
            n_valid += 1

    return n_valid

output = solve()
print(output)


