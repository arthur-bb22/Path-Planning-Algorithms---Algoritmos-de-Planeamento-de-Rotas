# Path-Planning-Algorithms---Algoritmos-de-Planeamento-de-Rotas
Here are some path planning algorithms that can be applied according to the intended context. The algorithms are A* in Python and C#, Theta* in Python, and FloodFill in C#. The heuristics used were Euclidean and Manhattan. The algorithm codes include a section dedicated to graphical visualization. 

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