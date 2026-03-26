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
    frames =[]
    frame_count = 0

    while open_set:
        _, current = heapq.heappop(open_set)

        if current == goal:
            path =[]
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

        for dx, dy in[(0,1),(1,0),(0,-1),(-1,0)]:
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

# Função para fazer animação modificada
def criar_animacao(mapa, frames_originais, filename='astar.gif'):
    fig, ax = plt.subplots()
    cmap = ListedColormap(['white', 'black']) 
    
    # Inicia a imagem com o mapa
    img = ax.imshow(mapa, cmap=cmap)
    path_line, = ax.plot([],[], 'b--', linewidth=2)  # caminho azul tracejado
    ax.set_title("A* Pathfinding")

    # PREPARAÇÃO DOS FRAMES:
    # Vamos reestruturar os frames para incluir a "fase" da animação
    frames_completos =[]
    
    # 1º Passo: Mostrar o mapa original por 2 segundos (fps=20 -> 40 frames)
    for _ in range(40):
        # A tupla agora é: (Fase, Visitados, Caminho)
        frames_completos.append(('mostrar_tudo', None, None))
        
    # 2º Passo: Adicionar os frames da exploração do A*
    for visitados, caminho in frames_originais:
        frames_completos.append(('explorar', visitados, caminho))


    def update(frame_data):
        fase, visitados, caminho = frame_data

        if fase == 'mostrar_tudo':
            # Mostra o mapa real (0=Branco, 1=Preto)
            img.set_data(mapa)
            path_line.set_data([],[])
            
        elif fase == 'explorar':
            # Cria a "névoa de guerra": uma matriz toda preta (cheia de 1s)
            tela_escura = np.ones_like(mapa)
            
            # Acende a luz onde o A* já visitou (transforma de 1 para 0)
            if visitados:
                for y, x in visitados:
                    tela_escura[y, x] = 0
            
            # Atualiza os dados da imagem (muito mais rápido que usar imshow de novo)
            img.set_data(tela_escura)

            # Se houver caminho no final, desenha a linha azul
            if caminho:
                ys, xs = zip(*caminho)
                path_line.set_data(xs, ys)
            else:
                path_line.set_data([], [])

        return [img, path_line]

    ani = animation.FuncAnimation(
        fig, update, frames=frames_completos, interval=100, blit=True, repeat=False
    )

    ani.save(filename, writer='pillow', fps=20)
    print(f"GIF salvo como: {filename}")

if __name__ == "__main__":
    mapa = gera_mapa(25, 25, perc_obstaculos=0.3)
    # Garante que início e fim estão livres
    mapa[0, 0] = 0 
    mapa[24, 24] = 0 
    
    path, frames = astar_animado(mapa, (0, 0), (24, 24))
    criar_animacao(mapa, frames, filename='astar0.gif')

    if path is None:
        print("caminho não encontrado")
    else:
        print(f"caminho encontrado com {len(path)} passos")