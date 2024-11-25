from collections import deque


def find_kate_in_maze(rows, maze):
    for r in range(rows):
        for c in range(len(maze[r])):
            if maze[r][c] == 'k':
                return r, c
    return None


def kate_escape(maze):
    rows = len(maze)
    cols = len(maze[0])

    # Find Kate's initial position
    start = find_kate_in_maze(rows, maze)
    if not start:
        return "Kate cannot get out"

    # Initialize BFS
    queue = deque([(start[0], start[1], 0)])  # (row, col, steps)
    visited = set([start])
    max_moves = 0
    escaped = False

    # Directions for movement: up, down, left, right
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while queue:
        x, y, steps = queue.popleft()

        # Check if Kate is at the edge (exit condition)
        if x == 0 or x == rows - 1 or y == 0 or y == cols - 1:
            escaped = True
            max_moves = max(max_moves, steps + 1)  # Update maximum moves

        # Explore neighbors
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if maze[nx][ny] == ' ':
                    queue.append((nx, ny, steps + 1))
                    visited.add((nx, ny))

    if escaped:
        return f"Kate got out in {max_moves} moves"
    else:
        return "Kate cannot get out"

n = int(input())
maze = [input() for _ in range(n)]


print(kate_escape(maze))
