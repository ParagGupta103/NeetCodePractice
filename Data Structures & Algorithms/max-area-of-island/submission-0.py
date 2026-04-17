class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows,cols = len(grid),len(grid[0])
        visited = set()
        max_area = 0

        def get_area(r,c):
            if not (r in range(rows) and c in range(cols)):
                return 0
            if grid[r][c] == 0:
                return 0
            if (r,c) in visited:
                return 0
            visited.add((r,c))
            return 1 + get_area(r+1,c) + get_area(r-1,c) + get_area(r,c+1) + get_area(r,c-1)

        

        for r in range(rows):
            for c in range(cols):
                area = get_area(r,c)
                if max_area < area:
                    max_area = area
        
        return max_area