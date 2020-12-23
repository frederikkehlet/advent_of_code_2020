with open('input.txt', 'r') as f:
     instructions = [line.strip() for line in f.readlines()]


def solve(instructions):
     visited_instructions = []
     accumulator = 0
     repeat = True
     i = 0

     while repeat:
          if i in visited_instructions or i >= len(instructions):
               repeat = False
          else:
               visited_instructions.append(i)
               operation = instructions[i].split(' ')[0]
               argument = instructions[i].split(' ')[1]

               if operation == 'acc':
                    i += 1
                    if argument[:1] == '+':
                         accumulator += int(argument[1:])                   
                    else:
                         accumulator -= int(argument[1:])
               elif operation == 'jmp':
                    if argument[:1] == '+':
                         i += int(argument[1:])
                    else:
                         i -= int(argument[1:])
               else:
                    i += 1 

     return accumulator, i

variations = []

for i in range(len(instructions)):  
     operation = instructions[i].split(' ')[0]
     argument = instructions[i].split(' ')[1]
     
     if operation == 'jmp':
          variation = list()
          variation = instructions.copy()
          variation[i] = 'nop ' + str(argument)
          variations.append(variation)
     elif operation == 'nop':
          variation = list()
          variation = instructions.copy()
          variation[i] = 'jmp ' + str(argument)
          variations.append(variation)

outputs = []

for variation in variations:
     outputs.append(solve(variation))

print(sorted(outputs, key = lambda x: x[1]))



