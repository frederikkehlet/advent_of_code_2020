lines  = []

with open('input.txt') as f:
    lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]

def solve():
    ids = []

    for line in lines:
        row_input = line[0:7]
        col_input = line[7:]

        row = get_row(row_input)
        col = get_col(col_input)
    
        id = row * 8 + col
        ids.append(id)

    return max(ids)
    

def get_row(row_input):
    binary = [0 if c == 'B' else 1 for c in row_input]
    decimal = int("".join(str(i) for i in binary),2)

    return 127 - decimal       

def get_col(col_input):
    binary = [0 if c == 'R' else 1 for c in col_input]
    decimal = int("".join(str(i) for i in binary),2)

    return 7 - decimal

output = solve()
print(output)