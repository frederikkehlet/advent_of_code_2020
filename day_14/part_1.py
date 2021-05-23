input = open('input.txt', 'r')
lines = input.readlines()
bitmask = ''
addressAndValues = {}

def encode(bitmask, binary):
    result = [b for b in binary]
    for i in range(len(bitmask)):
        if (bitmask[i] == '1' or bitmask[i] == '0') and (bitmask[i] != binary[i]):
            res = not bool(int(binary[i]))
            result[i] = str(int(res))   
    return ''.join(result)

def decimalTo36BitBinary(decimal):
    return bin(int(decimal)).replace("0b", "").zfill(36)

def solve():
    for line in lines:
        if 'mask' in line:
            bitmask = line.split(' = ')[1]
            continue
            
        memoryAddress = (line.split(' = ')[0])[4:-1]
        value = line.split(' = ')[1]

        addressAndValues[memoryAddress] = encode(bitmask,decimalTo36BitBinary(value))

    sum = 0
    for address in addressAndValues:
        sum += int(addressAndValues[address],2)
    return sum

answer = solve()
print(answer)

