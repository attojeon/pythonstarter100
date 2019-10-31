from sys import stdin

# display
def display_board():
    for line in board:
        print( line )

# settings
board = []

for x in range(19):
    line = []
    for y in range(19):
        line.append(0)
    board.append(line)

display_board()

print("어디에 바둑돌을 놓겠습니까? 1,3 과 같은 형식으로 입력하세요.")

running = True
while(running):
    inval = stdin.readline().strip().split(',')
    print(inval)
    row = int( inval[0])
    col = int( inval[1])

    board[row][col] = 9
    print(row, col)
    display_board()