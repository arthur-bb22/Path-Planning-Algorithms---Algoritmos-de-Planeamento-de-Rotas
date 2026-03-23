# A* Search Algorithm

A* (A-Star) is a heuristic-based search algorithm used to find the shortest path between a starting node and a target node. It is widely used due to its efficiency and optimality.

### Logic & Flow
The algorithm maintains two sets of nodes: `openSet` (nodes to be evaluated) and `closedSet` (nodes already evaluated).
1.  **Initialization**: Add the start node to the `openSet`.
2.  **Selection**: While the `openSet` is not empty, select the node with the lowest **fCost** ($f = g + h$).
    * $g$: Distance from the start node.
    * $h$: Estimated distance to the target (Heuristic).
3.  **Pathfinding**: If the selected node is the destination, the path is reconstructed via `RetracePath`.
4.  **Expansion**: If not, evaluate neighbors, calculate their costs, and update the `openSet`.

### Implementations
* **C# (Unity)**: Integrated as a `Pathfinder` asset. It uses the **Manhattan distance** ($|x_1 - x_2| + |y_1 - y_2|$) for grid-based efficiency.
* **Python**: A standalone script using `Numpy` for grid manipulation and `Matplotlib` for real-time path visualization.