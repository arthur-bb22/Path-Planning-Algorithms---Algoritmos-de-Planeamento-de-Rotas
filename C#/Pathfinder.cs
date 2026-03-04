using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public static class Pathfinder {
    public static List<Node> AStar(GridManager gridMgr, Node startNode, Node targetNode) {
        if (startNode == null || targetNode == null) return null;
        if (!startNode.walkable || !targetNode.walkable) return null;

        List<Node> openSet = new List<Node>();
        HashSet<Node> closedSet = new HashSet<Node>();

        openSet.Add(startNode);

        // reset parents and scores
        foreach (var n in gridMgr.grid) { n.parent = null; n.g = n.h = 0; }

        while (openSet.Count > 0) {
            Node current = openSet[0];
            for (int i=1;i<openSet.Count;i++) {
                if (openSet[i].f < current.f || (openSet[i].f == current.f && openSet[i].h < current.h)) current = openSet[i];
            }

            openSet.Remove(current);
            closedSet.Add(current);

            if (current == targetNode) {
                // retrace
                return RetracePath(startNode, targetNode);
            }

            foreach (var neighbor in gridMgr.GetNeighbors(current)) {
                if (!neighbor.walkable || closedSet.Contains(neighbor)) continue;

                int newCostToNeighbor = current.g + 1; // uniform cost
                if (newCostToNeighbor < neighbor.g || !openSet.Contains(neighbor)) {
                    neighbor.g = newCostToNeighbor;
                    neighbor.h = Heuristic(neighbor, targetNode);
                    neighbor.parent = current;

                    if (!openSet.Contains(neighbor)) openSet.Add(neighbor);
                }
            }
        }

        return null; // no path
    }

    static int Heuristic(Node a, Node b) {
        // Manhattan distance
        return Mathf.Abs(a.x - b.x) + Mathf.Abs(a.y - b.y);
    }

    static List<Node> RetracePath(Node start, Node end) {
        List<Node> path = new List<Node>();
        Node current = end;
        while (current != start) {
            path.Add(current);
            current = current.parent;
            if (current == null) break; // safety
        }
        path.Reverse();
        return path;
    }

    public static List<Node> FloodFill(GridManager gridMgr, Node startNode) {
        if (startNode == null || !startNode.walkable) return null;
        List<Node> visited = new List<Node>();
        Queue<Node> q = new Queue<Node>();
        HashSet<Node> seen = new HashSet<Node>();

        q.Enqueue(startNode); seen.Add(startNode);

        while (q.Count > 0) {
            var n = q.Dequeue();
            visited.Add(n);
            foreach (var nb in gridMgr.GetNeighbors(n)) {
                if (nb.walkable && !seen.Contains(nb)) {
                    seen.Add(nb);
                    q.Enqueue(nb);
                }
            }
        }
        return visited;
    }

    // ----- Coroutine versions for step-by-step visualization -----
    // Call these with StartCoroutine(...) from a MonoBehaviour (ex: InputController)

    public static IEnumerator AStarRoutine(GridManager gridMgr, Node startNode, Node targetNode, float stepDelay, Action<Node> onOpen=null, Action<Node> onClose=null, Action<Node> onVisit=null, Action<List<Node>> onFinish=null) {
        if (startNode == null || targetNode == null) { onFinish?.Invoke(null); yield break; }
        if (!startNode.walkable || !targetNode.walkable) { onFinish?.Invoke(null); yield break; }

        List<Node> openSet = new List<Node>();
        HashSet<Node> closedSet = new HashSet<Node>();

        openSet.Add(startNode);

        // initialize g to a large number so comparisons work
        foreach (var n in gridMgr.grid) { n.parent = null; n.g = n.h = int.MaxValue/4; }
        startNode.g = 0;
        startNode.h = Heuristic(startNode, targetNode);

        onOpen?.Invoke(startNode);
        yield return new WaitForSeconds(stepDelay);

        while (openSet.Count > 0) {
            Node current = openSet[0];
            for (int i=1;i<openSet.Count;i++) {
                if (openSet[i].f < current.f || (openSet[i].f == current.f && openSet[i].h < current.h)) current = openSet[i];
            }

            openSet.Remove(current);
            closedSet.Add(current);
            onClose?.Invoke(current);
            yield return new WaitForSeconds(stepDelay);

            if (current == targetNode) {
                var path = RetracePath(startNode, targetNode);
                onFinish?.Invoke(path);
                yield break;
            }

            foreach (var neighbor in gridMgr.GetNeighbors(current)) {
                if (!neighbor.walkable || closedSet.Contains(neighbor)) continue;

                int newCostToNeighbor = current.g + 1;
                if (newCostToNeighbor < neighbor.g || !openSet.Contains(neighbor)) {
                    neighbor.g = newCostToNeighbor;
                    neighbor.h = Heuristic(neighbor, targetNode);
                    neighbor.parent = current;

                    if (!openSet.Contains(neighbor)) {
                        openSet.Add(neighbor);
                        onOpen?.Invoke(neighbor);
                        yield return new WaitForSeconds(stepDelay);
                    }
                }
            }

            onVisit?.Invoke(current);
            yield return null;
        }

        onFinish?.Invoke(null);
    }

    public static IEnumerator FloodFillRoutine(GridManager gridMgr, Node startNode, float stepDelay, Action<Node> onVisit=null, Action<List<Node>> onFinish=null) {
        if (startNode == null || !startNode.walkable) { onFinish?.Invoke(null); yield break; }
        List<Node> visited = new List<Node>();
        Queue<Node> q = new Queue<Node>();
        HashSet<Node> seen = new HashSet<Node>();

        q.Enqueue(startNode); seen.Add(startNode);
        onVisit?.Invoke(startNode);
        yield return new WaitForSeconds(stepDelay);

        while (q.Count > 0) {
            var n = q.Dequeue();
            visited.Add(n);
            foreach (var nb in gridMgr.GetNeighbors(n)) {
                if (nb.walkable && !seen.Contains(nb)) {
                    seen.Add(nb);
                    q.Enqueue(nb);
                    onVisit?.Invoke(nb);
                    yield return new WaitForSeconds(stepDelay);
                }
            }
            yield return null;
        }

        onFinish?.Invoke(visited);
    }
}