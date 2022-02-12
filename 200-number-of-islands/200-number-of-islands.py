class Solution:
    def get_unvisited_neighbours(self, row, col, grid, visited):
        neighbours = []
        # up
        if row > 0 and not visited[row - 1][col] and grid[row - 1][col] != "0":
            neighbours.append((row - 1, col))
        # down
        if (
            row < len(grid) - 1
            and not visited[row + 1][col]
            and grid[row + 1][col] != "0"
        ):
            neighbours.append((row + 1, col))
        # left
        if col > 0 and not visited[row][col - 1] and grid[row][col - 1] != "0":
            neighbours.append((row, col - 1))
        # right
        if (
            col < len(grid[0]) - 1
            and not visited[row][col + 1]
            and grid[row][col + 1] != "0"
        ):
            neighbours.append((row, col + 1))

        for r, c in neighbours:
            visited[r][c] = True

        return neighbours

    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]
        islands = 0

        for r, c in product(range(rows), range(cols)):
            if visited[r][c] or grid[r][c] == "0":
                continue
            visited[r][c] = True
            q = deque([(r, c)])
            while q:
                r_, c_ = q.popleft()
                neighbors = self.get_unvisited_neighbours(r_, c_, grid, visited)
                q.extend(neighbors)

            islands += 1

        return islands
