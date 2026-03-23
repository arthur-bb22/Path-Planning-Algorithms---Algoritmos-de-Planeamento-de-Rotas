# Path Planning Algorithms

This repository features a collection of path planning algorithms designed for grid-based navigation, robotics, and game development. The project focuses on comparing different search strategies and visualization techniques across **Python** and **C# (Unity)**.

 | <img src="./Astar, Thetastar and FloodFill/Demonstrations/SimulationPython/gifs/astar3.gif" width="300" alt="A* Demo">|<img src="./Astar,%20Thetastar%20and%20FloodFill/Demonstrations/SimulationPython/gifs/theta_star1.gif" width="300" alt="Theta* Demo"> | 


## Project Structure
The repository is organized by algorithm to highlight their logic and implementation details:

* **[A* (A-Star)](./A-Star/)**: The gold standard for pathfinding. Includes implementations in both Python and C#.
* **[Theta*](./Theta-Star/)**: An "Any-Angle" pathfinding evolution of A* implemented in Python.
* **[Flood Fill](./Flood-Fill/)**: A grid-expansion algorithm implemented in C#.
* **[Demonstrations](./Demonstrations/)**: Visual results from Unity and VS Code simulations, including GIFs from VS Code (Matplotlib) plots.

## Technical Overview
| Algorithm | Language | Heuristic | Key Libraries/Tools |
| :--- | :--- | :--- | :--- |
| **A*** | C# / Python | Manhattan | Unity Engine / Numpy & Matplotlib |
| **Theta*** | Python | Euclidean | Bresenham's Algorithm |
| **Flood Fill**| C# | N/A | Queue-based Expansion |

---