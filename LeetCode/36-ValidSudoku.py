import collections
from typing import List

board=[[".",".","4",".",".",".","6","3","."],
[".",".",".",".",".",".",".",".","."],
["5",".",".",".",".",".",".","9","."],
[".",".",".","5","6",".",".",".","."],
["4",".","3",".",".",".",".",".","1"],
[".",".",".","7",".",".",".",".","."],
[".",".",".","5",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."],
[".",".",".",".",".",".",".",".","."]
]

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        boxes = collections.defaultdict(set)

        size = 9

        for r in range(size):
            for c in range(size):
                if board[r][c] == '.':
                    continue

                print(boxes)

                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in boxes[(r // 3,c // 3)]):
                    return False
                
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                boxes[(r//3,c//3)].add(board[r][c])
        

        return True


s = Solution()
print(s.isValidSudoku(board))  # Should return True or False based on the validity