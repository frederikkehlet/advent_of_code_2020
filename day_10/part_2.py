with open('input_test.txt', 'r') as f:
     adapters = sorted([int(line.strip('\n')) for line in f.readlines()])

res = 0

print(adapters)

for adapter in adapters:
     m = adapter
     for adapter in adapters:
          if adapter % m == 0:
               res += (adapter / m)

print(res)
     
