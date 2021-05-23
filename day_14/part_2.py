import itertools
input = open('input.txt', 'r')
lines = input.readlines()
bitmask = ''
addressAndValues = {}

def encode(bitmask, binary):
    result = [b for b in binary]
    for i in range(len(bitmask)):
        if bitmask[i] != '0': result[i] = bitmask[i] 
    return ''.join(result)

def decimalTo36BitBinary(decimal):
    return bin(int(decimal)).replace("0b", "").zfill(36)

def createAddressCopies(address):
    copies = []
    floatingBits = [b for b in address if b == 'X']
    for i in range(2 ** len(floatingBits)):
        copies.append(address)
    return copies

def createBitCombinations(address):
    floatingBits = [b for b in address if b == 'X']
    return list(itertools.product(range(2), repeat = len(floatingBits)))

def assignBitCombinationsToAddresses(combinations, copies): 
    addresses = []    
    for i in range(len(copies)):
        copy = list(copies[i])
        bits = list(combinations[i])
        j = 1
        for j in range(len(copy)):   
            if copy[-j] == 'X': 
                copy[-j] = str(bits[-1])
                bits.pop(-1)
        addresses.append(copy)  
    return [''.join(address) for address in addresses]

def solve():
    for line in lines:
        if 'mask' in line:
            bitmask = line.split(' = ')[1]
            continue
            
        memoryAddress = (line.split(' = ')[0])[4:-1]
        value = line.split(' = ')[1]
        binary = decimalTo36BitBinary(memoryAddress)        
        encodedAddress = encode(bitmask[:-1], binary)
        copies = createAddressCopies(encodedAddress)
        bits = createBitCombinations(encodedAddress)
        newAddresses = assignBitCombinationsToAddresses(bits, copies)
        
        for newAddress in newAddresses:
            addressAndValues[int(newAddress,2)] = value
    
    sum = 0
    for address in addressAndValues:
        sum += int(addressAndValues[address])
    return sum

answer = solve()
print(answer)




