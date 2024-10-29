class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        temp={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in board:
            d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
            for j in i:
                try:
                    if j==".":
                        continue
                    del d[j]
                except:
                    return False
        for i in range(9):
            d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
            try:
                for j in board:
                    if j[i]==".":
                        continue
                    del d[j[i]]
            except:
                return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(3):
            for j in range(3):
                try:
                    if board[i][j]==".":
                        continue
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(3,6):
            for j in range(3):
                try:
                    if board[i][j]==".":
                        continue
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(6,9):
            for j in range(3):
                try:
                    if board[i][j]==".":
                        continue
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(3):
            for j in range(3,6):
                if board[i][j]==".":
                    continue
                try:
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(3):
            for j in range(6,9):
                if board[i][j]==".":
                    continue
                try:
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(3,6):
            for j in range(3,6):
                if board[i][j]==".":
                    continue
                try:
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(3,6):
            for j in range(6,9):
                if board[i][j]==".":
                    continue
                try:
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(6,9):
            for j in range(3,6):
                if board[i][j]==".":
                    continue
                try:
                    del d[board[i][j]]
                except:
                    return False
        d={"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        for i in range(6,9):
            for j in range(6,9):
                if board[i][j]==".":
                    continue
                try:
                    del d[board[i][j]]
                except:
                    return False
        return True