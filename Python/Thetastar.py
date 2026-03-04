import numpy as np, heapq, matplotlib.pyplot as plt, matplotlib.animation as animation
from collections import namedtuple

Point = namedtuple('Point', ['y','x'])
inf = float('inf')

def euclid(a, b):
    return ((a.y-b.y)**2 + (a.x-b.x)**2)**0.5

def bresenham(a, b):
    y0, x0 = a.y, a.x
    y1, x1 = b.y, b.x
    dy = abs(y1 - y0); dx = abs(x1 - x0)
    sy = 1 if y1 > y0 else -1
    sx = 1 if x1 > x0 else -1
    err = dx - dy
    pts = []
    while True:
        pts.append(Point(y0, x0))
        if y0 == y1 and x0 == x1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy
    return pts

def line_of_sight(mapa, a, b):
    for p in bresenham(a, b):
        if mapa[p.y, p.x] != 0:
            return False
    return True

def theta_star(mapa, start, goal):
    open_set = [(0, start)]
    came_from = {start: None}
    g_score = {start: 0}
    f_score = {start: euclid(start, goal)}
    visited = set()
    frames = []
    frame_count = 0

    while open_set:
        _, current = heapq.heappop(open_set)
        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = came_from[current]
            path = path[::-1]

            # Adiciona o frame final com o caminho
            for _ in range(20):  # 1 segundo extra (20 fps)
                frames.append((visited.copy(), path))
            return path, frames

        visited.add(current)
        frame_count += 1
        if frame_count % 4 == 0:
            frames.append((visited.copy(), None))

        for dy, dx in [(0,1),(1,0),(0,-1),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]:
            nb = Point(current.y+dy, current.x+dx)
            if not (0 <= nb.y < mapa.shape[0] and 0 <= nb.x < mapa.shape[1]):
                continue
            if mapa[nb.y, nb.x] != 0:
                continue

            parent = came_from[current]
            if parent and line_of_sight(mapa, parent, nb):
                tentative_g = g_score[parent] + euclid(parent, nb)
                candidate_parent = parent
            else:
                tentative_g = g_score[current] + euclid(current, nb)
                candidate_parent = current

            if tentative_g < g_score.get(nb, inf):
                came_from[nb] = candidate_parent
                g_score[nb] = tentative_g
                f = tentative_g + euclid(nb, goal)
                f_score[nb] = f
                heapq.heappush(open_set, (f, nb))

    return None, frames

def criar_anim(mapa, path_frames, filename='theta_star.gif'):
    path, frames = path_frames
    fig, ax = plt.subplots()
    cmap = plt.get_cmap('gray_r', 2)  # atualizar
    img = ax.imshow(mapa, cmap=cmap)
    ln, = ax.plot([], [], 'b--', linewidth=2)
    ax.set_title("Θ* Pathfinding")

    def update(data):
        visitados, caminho = data
        overlay = np.zeros_like(mapa, dtype=float)
        for p in visitados:
            overlay[p.y, p.x] = 0.5
        img.set_data(mapa)
        img.set_alpha(1)
        ax.imshow(overlay, cmap='gray', alpha=0.5)

        if caminho:
            ys = [p.y for p in caminho]
            xs = [p.x for p in caminho]
            ln.set_data(xs, ys)
        else:
            ln.set_data([], [])
        return img, ln

    ani = animation.FuncAnimation(
        fig, update, frames=frames, interval=200, blit=True, repeat=False
    )
    ani.save(filename, writer='pillow', fps=20)
    print("GIF salvo como", filename)

if __name__ == "__main__":
    gera_mapa = lambda w,h,p=0.3: np.where(np.random.rand(h,w)<p, 1, 0)
    grid = gera_mapa(25, 25, 0.3)
    start, goal = Point(0, 0), Point(19, 19)
    path_frames = theta_star(grid, start, goal)
    criar_anim(grid, path_frames)
