with open('input.txt', 'r') as f:
     coordinates = [line.strip('\n') for line in f.readlines()]

compass_values = [0, 0, 0, 0] # EAST; NORTH; WEST; SOUTH

facing = 0

print(compass_values[1])

for coord in coordinates:
     direction = coord[0]
     value = coord[1:]

     if direction == 'N': # north
          compass_values[1] += int(value)
     elif direction == 'S': # south
          compass_values[3] += int(value)
     elif direction == 'E': # east
          compass_values[0] += int(value)
     elif direction == 'W': # west
          compass_values[2] += int(value)
     elif direction == 'L': # rotate left
          n_turns = int(value) / 90
          facing += n_turns % len(compass_values)
     elif direction == 'R': # rotate right
          n_turns = int(value) / 90
          facing -= n_turns % len(compass_values)
     elif direction == 'F': # move forward in facing direction
          compass_values[int(facing) % len(compass_values)] += int(value)

north_south = compass_values[3] - compass_values[1]
east_west = compass_values[2] - compass_values[0]

print(north_south + east_west)
