# Theta* (Any-Angle Path Planning)

Theta* is an optimization of the A* algorithm. While standard A* constrains movement to grid edges (resulting in "staircase" paths), Theta* allows for movement at any angle, producing smoother, more realistic trajectories.

### Line of Sight (LoS) & Bresenham
The core strength of Theta* is its ability to "look ahead":
* **Bresenham's Algorithm**: Used as a vision sensor to determine which grid cells are intersected by a straight line between two points.
* **Path Smoothing**: Instead of always connecting a node to its immediate neighbor, Theta* checks if there is a **Line of Sight** between the *parent* of the current node and the *neighbor*.
* **Result**: If the path is clear, it skips the current node and creates a direct diagonal or straight line, significantly reducing path segments.

### Heuristic
* **Euclidean Distance**: Unlike A* on a grid, Theta* requires the actual straight-line distance ($\sqrt{\Delta x^2 + \Delta y^2}$) because the movement is no longer restricted to 4 or 8 directions.

**Language:** Python (Numpy & Matplotlib)