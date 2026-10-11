# Snake AI that plays by itself using pathfinding (BFS) + a "never trap yourself" safety check
import pygame, random
from collections import deque

pygame.init()
COLS, ROWS, CS = 20, 20, 30
W, H = COLS * CS, ROWS * CS + 50
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("Snake AI")
clock = pygame.time.Clock()
font = pygame.font.SysFont("arial", 24, bold=True)


def nbrs(c):
    x, y = c
    for dx, dy in ((1, 0), (-1, 0), (0, 1), (0, -1)):
        nx, ny = x + dx, y + dy
        if 0 <= nx < COLS and 0 <= ny < ROWS:
            yield (nx, ny)


def bfs(start, goal, blocked):
    q, prev = deque([start]), {start: None}
    while q:
        c = q.popleft()
        if c == goal:
            path = []
            while c != start:
                path.append(c)
                c = prev[c]
            return path[::-1]
        for n in nbrs(c):
            if n not in prev and n not in blocked:
                prev[n] = c
                q.append(n)
    return None


def reachable(start, blocked):
    seen, q = {start}, deque([start])
    while q:
        for n in nbrs(q.popleft()):
            if n not in seen and n not in blocked:
                seen.add(n)
                q.append(n)
    return len(seen)


def spawn_food(body):
    free = [(x, y) for x in range(COLS) for y in range(ROWS) if (x, y) not in body]
    return random.choice(free) if free else None


def choose_move(body, food):
    head, tail = body[0], body[-1]
    # 1) shortest path to food, but only if the snake can still reach its tail afterwards
    path = bfs(head, food, set(body[:-1]))
    if path:
        virtual = (list(reversed(path)) + body)[:len(body) + 1]
        if bfs(virtual[0], virtual[-1], set(virtual[1:-1])) is not None or len(virtual) <= 2:
            return path[0]
    # 2) chase the tail (always safe)
    path = bfs(head, tail, set(body[1:-1]))
    if path:
        return path[0]
    # 3) any move that keeps the most space open
    best, best_space = None, -1
    for n in nbrs(head):
        if n not in body[:-1]:
            space = reachable(n, set(body[:-1]))
            if space > best_space:
                best, best_space = n, space
    return best


def new_game():
    body = [(COLS // 2, ROWS // 2)]
    return body, spawn_food(body)


body, food = new_game()
best, games, fps = 0, 1, 30

running = True
while running:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
            if e.key == pygame.K_UP:
                fps = min(fps * 2, 480)
            if e.key == pygame.K_DOWN:
                fps = max(fps // 2, 5)

    move = choose_move(body, food) if food else None
    if move is None:
        best = max(best, len(body))
        body, food = new_game()
        games += 1
        continue

    body.insert(0, move)
    if move == food:
        food = spawn_food(body)
    else:
        body.pop()

    screen.fill((15, 15, 25))
    for x in range(COLS):
        for y in range(ROWS):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, (22, 22, 36), (x * CS, y * CS, CS, CS))
    if food:
        pygame.draw.circle(screen, (255, 70, 90), (food[0] * CS + CS // 2, food[1] * CS + CS // 2), CS // 2 - 3)
    for i, (x, y) in enumerate(body):
        t = i / max(len(body), 1)
        color = (int(60 - 40 * t), int(255 - 130 * t), int(120 - 40 * t))
        pygame.draw.rect(screen, color, (x * CS + 2, y * CS + 2, CS - 4, CS - 4), border_radius=8)
    screen.blit(font.render(f"Length {len(body)}   Best {max(best, len(body))}   Game {games}",
                            True, (255, 255, 255)), (12, ROWS * CS + 12))
    pygame.display.flip()
    clock.tick(fps)

pygame.quit()