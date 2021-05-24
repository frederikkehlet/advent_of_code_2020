input = open('input.txt', 'r')
lines = input.readlines()
sections = []

def solve():
    i = 0
    j = 0
    while i < len(lines):
        if lines[i] == "\n":
            sections.append(lines[j:i])
            j = i + 1
        i += 1      
    sections.append(lines[j:i])

    #first section contains all possible valid fields
    fields = [field.split(" ") for field in sections[0]]
    values = []
    for field in fields:
        for val in field:
            if "-" in val:
                values.append(val)

    valueRange = [val.split("-") for val in values]
    validValues = []

    def fill(min, max):
        arr = []
        min += 1
        while min <= max:
            arr.append(min)
            min += 1
        return arr

    for range in valueRange:
        min = int(range[0])
        max = int(range[1])

        filledRange = fill(min,max)
        i = 0
        while i < len(filledRange):
            range.append(filledRange[i])
            i += 1

        range.append(range[i])
        del range[1]

        for n in range: 
            validValues.append(int(n))

    #second section contains my ticket

    #third sections contains nearby tickets
    nearbyTickets = sections[2][1:]
    ticketRanges = list(''.join(nearbyTickets).split("\n"))

    tickets = []
    [tickets.append(range.split(",")) for range in ticketRanges]

    invalidValues = []
    for ticket in tickets:
        for val in ticket:
            if int(val) not in validValues:
                invalidValues.append(int(val))

    return sum(invalidValues)

answer = solve()
print(answer)

        