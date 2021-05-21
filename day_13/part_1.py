input = open('input.txt', 'r')
lines = input.readlines()

startingEstimate = int(lines[0])
finalEstimate = startingEstimate
ids = lines[1].split(',')

busNotFound = True
firstCheck = True

availableBusId = None
while busNotFound: 
    if not firstCheck: finalEstimate += 1
    for id in ids:
        if id != 'x' and finalEstimate % int(id) == 0:
            availableBusId = id
            busNotFound = False
            break
    firstCheck = False
    

differenceMinutes = finalEstimate - startingEstimate
answer = differenceMinutes * int(availableBusId)

print(answer)