def find_max_diamonds(grid,R,H):
    def dfs(row, col):
        if not (0 <= row < R) or not (0 <= col < H) or grid[row][col] == '#' or grid[row][col] == 'V':
            return 0

        diamonds = 0
        if grid[row][col] == 'D':
            diamonds = 1

        grid[row][col] = 'V'  # Mark the cell as visited

        diamonds += dfs(row, col + 1)  # Right
        diamonds += dfs(row, col - 1)  # Left
        diamonds += dfs(row + 1, col)  # Down
        diamonds += dfs(row - 1, col)  # Up

        return diamonds

    max_diamonds = 0
    for r in range(R):
        for h in range(H):
            if grid[r][h] == '.':
                max_diamonds = max(max_diamonds, dfs(r, h))

    return max_diamonds


f1 = open('input-6.txt', 'r')
f2 = open('output-6.txt', 'w')

r,h = map(int, f1.readline().split())
grid = []

for i in range(r):
    l = list(f1.readline().strip())
    grid.append(l)

print(grid)
print(find_max_diamonds(grid,r,h),file=f2)

f1.close()
f2.close()