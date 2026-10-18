class Solution:
    def lastVisitedCell(self, grid: list[list[str]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])
        last_visited = (0, 0)
        visited = set()
        visited.add(last_visited)
        r, c = 0, 0
        while True:
            if grid[r][c] == 'L':
                c -= 1
            elif grid[r][c] == 'R':
                c += 1
            elif grid[r][c] == 'U':
                r -= 1
            else:
                r += 1
            if 0 <= r < m and 0 <= c < n:
                if (r, c) in visited:
                    break
                else:
                    visited.add((r, c))
                    last_visited = (r, c)
            else:
                break
        return last_visited