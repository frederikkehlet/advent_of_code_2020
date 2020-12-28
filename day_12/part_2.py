import numpy as np

with open('input.txt', 'r') as f:
     coordinates = [line.strip('\n') for line in f.readlines()]

waypoint = np.array([1, 10, 0, 0]) #NORTH, EAST, SOUTH, WEST
coords = [0,0,0,0] #NORTH, EAST, SOUTH, WEST

for coord in coordinates:
     direction = coord[0]
     value = coord[1:]

     if direction == 'N':
          waypoint[0] = (waypoint[0] + int(value))
     elif direction == 'S':
          waypoint[2] = (waypoint[2] + int(value))
     elif direction == 'E':
          waypoint[1] = (waypoint[1] + int(value))
     elif direction == 'W':
          waypoint[3] = (waypoint[3] + int(value))
     elif direction == 'L':
          n = int(value) / 90
          waypoint = np.roll(waypoint,int(-n))
     elif direction == 'R':
          n = int(value) / 90
          waypoint = np.roll(waypoint, int(n))
     elif direction == 'F':
          for i in range(4):
               coords[i] += int(value) * waypoint[i]
          
north_south = coords[0] - coords[2] if coords[0] > coords[2] else coords[2] - coords[0]
east_west = coords[1] - coords[3] if coords[1] > coords[3] else coords[3] - coords[1]

print(north_south + east_west)





