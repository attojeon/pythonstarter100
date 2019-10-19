

# settings
board = []
line = []
for x in range(19):
    line = []
    for y in range(19):
        line.append(0)
    board.append(line)

# display

for line in board:
    print('{}\n'.format( line))
    
