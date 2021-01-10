class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        xLen = len(grid)
        if xLen == 0:
            return 0
        yLen = len(grid[0])
        result = 0
        for i in range(xLen):
            for j in range(yLen):
                if grid[i][j] == '1':
                    result += 1
                    self.waterIslands(grid, i, j, xLen, yLen)
        return result

    def waterIslands(self, grid: List[List[str]], x: int, y: int, xLen: int, yLen: int):
        if x < 0 or x >= xLen or y < 0 or y >= yLen or grid[x][y] != '1':
            return
        grid[x][y] = '0'
        self.waterIslands(grid, x - 1, y, xLen, yLen)
        self.waterIslands(grid, x, y - 1, xLen, yLen)
        self.waterIslands(grid, x + 1, y, xLen, yLen)
        self.waterIslands(grid, x, y + 1, xLen, yLen)
