class Solution:
    def exist(self, board, word):
        limit = len(word)
        n = len(board)
        m = len(board[0])
        path = set()

        def dfs(x, y, idx):
            if idx == limit:
                return True
            if x < 0 or x >= n or \
                    y < 0 or y >= m or \
                    (x, y) in path or \
                    word[idx] != board[x][y]:
                return False

            path.add((x, y))
            res = (dfs(x+1, y, idx + 1) or
                   dfs(x-1, y, idx + 1) or
                   dfs(x, y+1, idx + 1) or
                   dfs(x, y-1, idx + 1))
            path.remove((x, y))
            return res

        for x in range(n):
            for y in range(m):
                if board[x][y] == word[0]:
                    if dfs(x, y, 0):
                        return True
        return False


S = Solution()
print(S.exist(board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"))