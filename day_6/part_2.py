groups = []

with open('input.txt', 'r') as f:
    lines = f.read()
    groups = lines.split("\n\n")
    groups = [group.replace('\n', ' ') for group in groups]

def solve():
    total_count = 0
    for group in groups:
        sets = [set(x) for x in list(group.split(' '))]
        answers_all = set.intersection(*sets)
        total_count += len(answers_all)    
    return total_count

print(solve())
