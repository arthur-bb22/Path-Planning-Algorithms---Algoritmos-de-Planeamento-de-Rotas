# Path-Planning-Algorithms---Algoritmos-de-Planeamento-de-Rotas
Presented here are some path planning algorithms, which can be applied according to the intended context. The algorithms are A* in Python and C#, Theta* in Python, and FloodFill in C#. The heuristics used were Euclidean and Manhattan. Within the algorithm codes, there is a section dedicated to the graphical visualization of the algorithm.

In the C# folder, the file contains 2 algorithms: A* and FloodFill. This file was taken from the full simulation in Unity; in other words, it is an asset that was named Pathfinder.

In the A portion:* The heuristic used was Manhattan and the language used was C#. The A* flow works as follows: it adds the starting point to an openSet; while there are nodes in the list, it takes the node with the lowest total cost. If this node is the destination, it reconstructs the path back (RetracePath). If not, it looks at the neighbors, calculates their costs, and adds them to the list to be visited.

In the FloodFill part: It works like the "paint bucket" tool in Paint. It uses a Queue to visit one neighbor at a time, spreading like an oil slick until it finds no more free paths.

In the Python folder, there are the following 2 algorithms: A* and Theta*.

In A:* The algorithm is identical to the C# one, but made with the Python language and utilizes libraries present in Python, such as numpy and matplotlib.

In Theta:* The algorithm uses a "vision sensor," and for this, it uses the Bresenham algorithm, which calculates which "pixels" (or grid squares) a straight line crosses to go from point A to point B. It also uses line_of_sight, which uses Bresenham to check each of these squares. If it finds an obstacle (!= 0), it returns False. If the path is clear, it says there is "line of sight." Then, instead of always connecting the current node to its immediate neighbor, Theta* looks at the parent of the current node. If there is a line of sight between the current node's parent and the neighbor, it ignores the current node and creates a straight line. This avoids that "staircase" jagged movement, as seen in A*. The heuristic used in this algorithm is Euclidean; this is necessary because the angles are now free, so we need the real distance between two points in space.

In the Demonstrations folder are some images of the simulation in Unity and images of the simulation in VS CODE, along with some GIFs of the algorithms being used.

////

Aqui estão apresentados alguns algoritmos de planeamento de caminhos, podem ser aplicados comforme o contexto pretendido. Os algoritmos são A* em Python e em C#, Theta* em Python e FloodFill em C#. As heurísticas usadas foram a euclidiana e a de Manhattan. Há nos códigos dos algoritmos uma parte que é dedicada a visualização gráfica do algoritmo. 

Na pasta C#, no arquivo há 2 algoritmos: o A* e o FloodFill. Esse arquivo foi retirado da simulação completa no Unity, ou seja, é um asset que foi denominado como Pathfinder. 

Na porção do A*: a heurística usada foi a manhattan e a linguagem utilizada foi o C#. O fluxo do A* funciona da seguinte forma: ele adiciona o ponto inicial em uma openSet,enquanto houver nós na lista ele pega o nó com o menor custo total. Se esse nó for o destino, ele reconstrói o caminho de volta (RetracePath).Se não, olha os vizinhos, calcula os custos deles e os adiciona na lista para serem visitados.

Na parte do FloodFill: Funciona como a ferramenta de "balde de tinta" do Paint. Ele usa uma Queue para visitar um vizinho de cada vez, espalhando-se como uma mancha de óleo até não encontrar mais caminhos livres. 

Na pasta Python, estão os 2 seguinte algoritmos: o A* e o Theta*.

No A*: O algoritmo é idêntico ao do C#, porém feito com a linguagem Python e utiliza de bibliotecas presentes no Python, como o numpy e o matplotlib.

No Theta*: O algoritmo usa um "sensor de visão" e para isso ele usa o algoritmo Bresenham que calcula quais "pixels" (ou quadrados da grade) fazem uma linha reta atravessa para ir de um ponto A até um ponto B. Ele também usa line_of_sight que usa o Bresenham para checar cada um desses quadrados. Se encontrar um obstáculo (!= 0), ele retorna False. Se o caminho estiver limpo, ele diz que há "linha de visão". Depois em vez de sempre ligar o nó atual ao seu vizinho imediato, o Theta* olha para a origem do nó atual. Se houver linha de visão entre a origem do nó atual e o vizinho, ele ignora o nó atual e faz uma linha reta. Isso evita aquele movimento "serrilhado" de escada, como no A*.
A heurística utilizada nesse algoritmo é a euclidiana, isso é necessário porque agora os ângulos são livres, então precisamos da distância real entre dois pontos no espaço.

Na pasta Demonstrations estão algumas imagens da simulação no Unity e as imagens da simulação no VSCODE juntamente com alguns GIFs dos algoritmos sendo usados.