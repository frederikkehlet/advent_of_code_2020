lines = []

with open('input.txt') as f:
    lines = f.readlines()
    lines = [l.replace('\n', '') for l in lines]


def solve():
    actual_ids = []
    possible_ids = []

    for line in lines:
        actual_ids.append(get_id(line))

    for row in range(0,127):
        for col in range(0,7):
            id = row * 8 + col

            if id not in actual_ids:
                possible_ids.append(id)

    return possible_ids


def get_id(line):
    row_input = line[0:7]
    col_input = line[7:]

    row = get_row(row_input)
    col = get_col(col_input)

    id = row * 8 + col
    return id


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
