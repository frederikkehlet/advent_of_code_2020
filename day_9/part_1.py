with open('input.txt', 'r') as f:
     numbers = [int(l.strip('\n')) for l in f.readlines()]

def solve():
     tail = 0
     head = 25

     for i in range(head, len(numbers)):
          past_25 = numbers[tail:i]
          current_num = int(numbers[i])
          adds_up = False

          for j in past_25:
               for k in past_25:
                    if (j + k == current_num) and (j != k):
                         adds_up = True

          if adds_up:
               tail += 1  
          else:
               return current_num

output = solve()
print(output)

