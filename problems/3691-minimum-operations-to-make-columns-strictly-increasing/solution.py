class Solution:
    def minimumOperations(self, grid):
        m = len(grid)
        n = len(grid[0])
        operations = 0

        for j in range(n):
            for i in range(1, m):
                if grid[i][j] <= grid[i - 1][j]:
                    needed = grid[i - 1][j] + 1 - grid[i][j]
                    operations += needed
                    grid[i][j] += needed

        return operations
