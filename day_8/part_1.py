with open('input.txt', 'r') as f:
     instructions = [line.strip() for line in f.readlines()]

visited_instructions = []
accumulator = 0

instruction_not_repeated = True
i = 0

while instruction_not_repeated:
     if i in visited_instructions:
         instruction_not_repeated = False
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

print(accumulator)
              
          



