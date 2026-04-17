class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        rows,cols = len(grid),len(grid[0])
        count = 0
        visited = set()

        def bfs(r,c):
            q = collections.deque()
            visited.add((r,c))
            q.append((r,c))
            while q:
                row,col = q.popleft()
                dirn = [[1,0],[-1,0],[0,1],[0,-1]]
                for dr, dc in dirn:
                    new_r,new_c = row+dr,col+dc
                    if (
                        new_r in range(rows) and
                        new_c in range(cols) and
                        grid[new_r][new_c] == "1" and
                        (new_r,new_c) not in visited
                    ):
                        q.append((new_r,new_c))
                        visited.add((new_r,new_c))
        
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    bfs(r,c)
                    count+=1
        return count