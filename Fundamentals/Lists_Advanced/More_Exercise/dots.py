def find_largest_connected_dots(board):
    rows = len(board)
    cols = len(board[0])
    visited = [[False] * cols for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    def is_valid(r, c):
        """Check if a position is valid for traversal."""
        return 0 <= r < rows and 0 <= c < cols and not visited[r][c] and board[r][c] == '.'

    def dfs(r, c):
        """Perform DFS to count connected dots."""
        stack = [(r, c)]
        visited[r][c] = True
        count = 1
        while stack:
            cr, cc = stack.pop()
            for dr, dc in directions:
                nr, nc = cr + dr, cc + dc
                if is_valid(nr, nc):
                    visited[nr][nc] = True
                    stack.append((nr, nc))
                    count += 1
        return count

    max_connected = 0

    for r in range(rows):
        for c in range(cols):
            if board[r][c] == '.' and not visited[r][c]:
                max_connected = max(max_connected, dfs(r, c))

    return max_connected


n = int(input())
board = [input().split() for _ in range(n)]

result = find_largest_connected_dots(board)

print(result)
