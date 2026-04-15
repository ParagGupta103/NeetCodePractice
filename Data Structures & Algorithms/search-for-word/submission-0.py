class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def get_neighbors_tuples(board, r, c):
            rows, cols = len(board), len(board[0])
            return [
                (board[nr][nc], nr, nc) 
                for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
                if 0 <= nr < rows and 0 <= nc < cols
            ]
        
        visited = set()
        def backtrack(word_index,row,col):
            if word_index == len(word):
                return True
            
            if (row, col) in visited or board[row][col] != word[word_index]:
                return False
            
            if word_index == len(word) - 1:
                return True
            
            visited.add((row, col))
            neighbours = get_neighbors_tuples(board,row,col)
            for n in neighbours:
                if backtrack(word_index + 1, n[1], n[2]):
                    return True
            visited.remove((row, col))
            return False
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(0, r, c):
                    return True
        return False