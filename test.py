board = []
line = []
for x in range(19):
    board = []
    for y in range(19):
        line.append(0)
    board.append(line)


for x in range(19):
    line = board[x]
    print(line)
    print('\n')
    
