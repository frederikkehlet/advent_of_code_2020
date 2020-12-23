with open('input.txt', 'r') as f:
     numbers = [(int(l.strip('\n'))) for l in f.readlines()]

invalid_num = 50047984

def get_contiguous_set():   
     for i in range(0, len(numbers)):
          j = i + 1

          while sum(numbers[i:j]) <= invalid_num:
               if sum(numbers[i:j]) == invalid_num:
                    return numbers[i:j]
               else:
                    j += 1

          if sum(numbers[i:j]) == invalid_num:
               return numbers[i:j]

set = get_contiguous_set()
set = sorted(set)

output = set[0] + set[-1]
print(output)
     








