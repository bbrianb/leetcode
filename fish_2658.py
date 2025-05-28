class Solution:
    # noinspection PyPep8Naming,PyMethodMayBeStatic
    def findMaxFish(self, grid: list[list[int]]) -> int:
        possibilities = []
        gridSize = len(grid)*len(grid[0])
        nonTails = nonGroups = 0
        while nonTails < gridSize or nonGroups < gridSize:
            if nonTails < gridSize:
                nonTails = 0
            if nonGroups < gridSize:
                nonGroups = 0
            for r, row in enumerate(grid):
                for c, cell in enumerate(row):
                    nonTails += 1
                    if nonTails >= gridSize:
                        nonGroups += 1
                    if cell != 0:
                        neighbors: list = []
                        corners: list = []
                        left = right = up = down = False
                        if c != len(row) - 1 and grid[r][c+1] != 0:
                            right = True
                            neighbors.append((r,c+1))
                        if c != 0 and grid[r][c-1] != 0:
                            left = True
                            neighbors.append((r,c-1))
                        if r != len(grid) - 1 and grid[r+1][c] != 0:
                            down = True
                            neighbors.append((r+1,c))
                        if r != 0 and grid[r-1][c] != 0:
                            up = True
                            neighbors.append((r-1,c))
                        if down and right:
                            corners.append((r+1, c+1))
                        if down and left:
                            corners.append((r+1, c-1))
                        if up and right:
                            corners.append((r-1, c+1))
                        if up and left:
                            corners.append((r-1, c-1))
                        for corner in corners:
                            r2 = corner[0]
                            c2 = corner[1]
                            if grid[r2][c2] == 0:
                                corners.remove(corner)
                        if len(neighbors) == 1 or len(neighbors) == 2 and len(corners) == 1 and nonTails >= gridSize:
                            r3 = neighbors[0][0]
                            c3 = neighbors[0][1]
                            grid[r3][c3] += cell
                            grid[r][c] = 0
                            nonTails = 0
                            nonGroups = 0
                        elif len(neighbors) == 0:
                            possibilities.append(cell)
                            grid[r][c] = 0

        output = 0
        for r in grid:
            for c in r:
                output += c
        if possibilities:
            return max(output, max(possibilities))
        else:
            return output


test_cases = (
    {'input': ([[0,2,1,0],[4,0,0,3],[1,0,0,4],[0,3,2,0]], ), 'output': 7},
    {'input': ([[0]], ), 'output': 0},
    {'input': ([[8,6],[2,6]], ), 'output': 22},
    {'input': ([[0,3,7],[0,5,1]], ), 'output': 16},
    {'input': ([[6,1,0,10],[5,3,0,0]], ), 'output': 15},
    {'input': ([[7,6,5,10,8],[0,0,10,8,6],[10,10,0,0,2],[9,4,4,0,1],[10,7,0,3,0]], ), 'output': 63},
    {'input': ([[2,8,6,6,0],[0,0,2,1,0],[0,0,0,0,5],[0,2,6,2,0],[0,0,1,1,0]], ), 'output': 25},
    {'input': ([[8,0,9,5,0],[6,10,4,8,4],[0,1,0,0,7],[1,10,6,7,10],[7,10,7,2,8]], ), 'output': 130},
    {'input': ([[10,1,10,10,5],[6,0,0,7,3],[6,2,4,0,9],[9,2,1,3,0],[0,10,3,5,4]], ), 'output': 110},
    {'input': ([[0,0,0,0,9,0,0,5],[3,9,0,3,0,0,8,0],[0,0,0,5,0,7,0,0],[0,0,8,6,4,4,9,0],[3,0,7,0,10,0,2,2],[0,0,10,4,2,0,1,7],[9,4,4,2,0,1,0,0]], ), 'output': 110}
)