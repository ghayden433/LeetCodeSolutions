class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        def square(i, j):
            result = list()
            for h in range(3):
                for k in range(3):
                    if board[h+i][k+j].isnumeric():
                        result.append(board[h+i][k+j])
            if len(result) == len(set(result)):
                return True
            return False
        
        def horizontal(i):
            result = list()
            for h in range(9):
                if board[i][h].isnumeric():
                    result.append(board[i][h])
            if len(result) == len(set(result)):
                return True
            return False
        
        def vertical(i):
            result = list()
            for h in range(9):
                if board[h][i].isnumeric():
                    result.append(board[h][i])
            print(result)
            if len(result) == len(set(result)):
                return True
            return False

        for i in range(9):
            if vertical(i) == False or horizontal(i) == False:
                return False
        
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if square(i, j) == False:
                    return False
        
        return True