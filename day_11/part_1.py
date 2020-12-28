with open('input.txt', 'r') as f:
     rows = [list(l.strip('\n')) for l in f.readlines()]

global total_rows, total_cols
total_rows = len(rows)
total_cols = len(rows[0])

def n_occupied_seats(rows, row, seat):
     n_occupied = 0
     for i in range(-1,2):
          for j in range(-1,2):
               if row+i >= 0 and row+i < total_rows and seat+j >= 0 and seat+j < total_cols: #valid index
                    if rows[row+i][seat+j] == '#':
                         n_occupied += 1
     return n_occupied - 1 if rows[row][seat] == '#' else n_occupied

seats_have_changed = True
while seats_have_changed:
     new_rows = []
     for row in range(total_rows):
          seats = []
          for seat in range(total_cols):
               if rows[row][seat] == 'L' and n_occupied_seats(rows, row, seat) == 0:
                    seats.append('#')
               elif rows[row][seat] == '#' and n_occupied_seats(rows, row, seat) >= 4:
                    seats.append('L')
               else:
                    seats.append(rows[row][seat])
          new_rows.append(seats)
   
     if rows == new_rows: seats_have_changed = False
     else: rows = new_rows

n_occupied_seats_final = 0
for row in rows: 
     n_occupied_seats_final += sum([r.count('#') for r in row])
print(n_occupied_seats_final)




