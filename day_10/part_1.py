with open('input.txt', 'r') as f:
     adapters = sorted([int(line.strip('\n')) for line in f.readlines()])

device_rating = adapters[-1] + 3
effective_rating = 0
differences_1 = []
differences_3 = []

while effective_rating < device_rating:
     possible_adapters = []
     
     for adapter in adapters:
          if (adapter == effective_rating + 1) or (adapter == effective_rating + 2) or (adapter == effective_rating + 3):
               possible_adapters.append(adapter)

     if len(possible_adapters) == 0: break

     new_effective_rating = possible_adapters[0]

     difference = new_effective_rating - effective_rating
     differences_1.append(difference) if difference == 1 else differences_3.append(difference)    
     effective_rating = new_effective_rating

#we add an extra 3 rating difference for the difference between the highest rated adapter and the device
print(len(differences_1) * (len(differences_3) + 1)) 