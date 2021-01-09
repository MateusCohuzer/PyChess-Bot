class ChessBoard:
    def __init__(self):
        pass

    def setBoard(self):
        self.boardDict = dict()
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        for i in range(1, 9):
            for j in letters:
                self.boardDict[f'{j}{i}'] = ''
        return self.boardDict
    
    def organizePieces(self):
        

Board = ChessBoard()
print(Board)
