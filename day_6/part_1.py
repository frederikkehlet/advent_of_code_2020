groups = []

with open('input.txt', 'r') as f:
    lines = f.read()
    groups = lines.split("\n\n")
    groups = [group.replace('\n', ' ') for group in groups]

def solve():
    total_count = 0

    for group in groups:
        all_answers = group.replace(' ', '')

        total_count += len(set(all_answers))

    return total_count

output = solve()
print(output)
    
    
