# Flood Fill Algorithm

Flood Fill is an algorithm primarily used to determine the area connected to a given node in a multi-dimensional array. In path planning, it is often used for map exploration or "filling" reachable areas.

### "Oil Slick" Expansion
The algorithm works similarly to the "Paint Bucket" tool in graphic editors:
* **Queue-based Approach**: It uses a FIFO (First-In-First-Out) queue to visit neighbors systematically.
* **Unweighted Search**: Unlike A*, it doesn't use a heuristic; it simply spreads outward until it hits boundaries or obstacles.
* **Use Case**: This implementation was extracted from a Unity simulation to demonstrate area coverage and reachability checks.

**Language:** C# (Unity Asset)