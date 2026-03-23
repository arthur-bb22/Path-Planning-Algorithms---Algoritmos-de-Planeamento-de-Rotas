import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import heapq
from matplotlib.colors import ListedColormap

def gera_mapa(largura, altura, perc_obstaculos=0.4):
    mapa = np.zeros((altura, largura), dtype=int)
    obst = np.random.rand(altura, largura) < perc_obstaculos
    mapa[obst] = 1
    return mapa

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def astar_animado(mapa, start, goal):
    open_set = [(0, start)]
    came_from = {}
    g_score = {start: 0}
    visited = set()
    frames = []
    frame_count = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path = path[::-1]
            frames.append((visited.copy(), path))
            for _ in range(40):  # adiciona 2 segundos extras pra poder ver o gif no final
                frames.append((visited.copy(), path))
            return path, frames

        if current in visited:
            continue
        visited.add(current)
        
        if len(visited) % 100 == 0:
            print(f"Visitados: {len(visited)}")
        
        frame_count += 1
        if frame_count % 4 == 0:
            frames.append((visited.copy(), None))

        for dx, dy in [(0,1),(1,0),(0,-1),(-1,0)]:
            vizinho = (current[0]+dy, current[1]+dx)
            if (0 <= vizinho[0] < mapa.shape[0] 
                and 0 <= vizinho[1] < mapa.shape[1] 
                and mapa[vizinho] == 0):
                tentative_g = g_score[current] + 1
                if tentative_g < g_score.get(vizinho, float('inf')):
                    came_from[vizinho] = current
                    g_score[vizinho] = tentative_g
                    f = tentative_g + heuristica(vizinho, goal)
                    heapq.heappush(open_set, (f, vizinho))

    frames.append((visited.copy(), None))
    return None, frames

# função para fazr animação
def criar_animacao(mapa, frames, filename='astar.gif'):
    fig, ax = plt.subplots()
    cmap = ListedColormap(['white', 'black']) 
    img = ax.imshow(mapa, cmap=cmap)
    path_line, = ax.plot([], [], 'b--', linewidth=2)  # caminho azul tracejado
    ax.set_title("A* Pathfinding")

    def update(frame_data):
        visitados, caminho = frame_data
        overlay = np.zeros_like(mapa, dtype=float)

        for y, x in visitados:
            overlay[y, x] = 0.5  

        img.set_data(mapa)
        img.set_alpha(1.0)
        ax.imshow(overlay, cmap='gray', alpha=0.5)

        if caminho:
            ys, xs = zip(*caminho)
            path_line.set_data(xs, ys)
        else:
            path_line.set_data([], [])

        return [img, path_line]

    ani = animation.FuncAnimation(
        fig, update, frames=frames, interval=100, blit=True, repeat=False
    )

    ani.save(filename, writer='pillow', fps=20)
    print(f"GIF salvo como: {filename}")

if __name__ == "__main__":
    mapa = gera_mapa(25, 25, perc_obstaculos=0.3)
    path, frames = astar_animado(mapa, (0, 0), (24, 24))
    criar_animacao(mapa, frames, filename='astar0.gif')

if path is None:
    print("caminho não encontrado")
else:
    print(f"caminho encontrado com {len(path)} passos")