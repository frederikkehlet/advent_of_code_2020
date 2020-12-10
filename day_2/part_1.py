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
        min_max = policy_split[0].split('-')
        char = policy_split[1]
        mn = int(min_max[0])
        mx = int(min_max[1])
        counter = pwd.count(char)

        if (mn <= counter <= mx):
            n_valid += 1

    return n_valid

output = solve()
print(output)


