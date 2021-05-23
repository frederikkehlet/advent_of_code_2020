input = open('input.txt', 'r')
lines = input.readlines()
ids = lines[1].split(',')
sequenceNotFound = True
t = 0

idsAndConstraints = {}
for id in ids:
    if id !='x': 
        idsAndConstraints.update({int(id): ids.index(id)})


