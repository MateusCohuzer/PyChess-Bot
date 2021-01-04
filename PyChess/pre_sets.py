def setBoard():
    board = dict()
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    for i in range(1, 9):
        for j in letters:
            board[f'{j}{i}'] = ''
    return board

print(setBoard())
