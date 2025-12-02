## Summary:

You are asked to help a reindeer fill in missing hiking trails on a topographic map of a floating island. The map represents heights ranging from `0` (lowest) to `9` (highest). A hiking trail should start from height `0`, end at `9`, and each step should have an increment of `1` without any diagonal movement. A starting position, denoted `0`, is considered a trailhead and it is assigned a score equivalent to the number of `9`s reachable from it, following the hiking trail rules. Your task is to calculate the sum of scores of all trailheads on your given topographic map.

## Inputs:

The input is a grid (or a 2D array) of integers ranging from 0 to 9, representing the topographic map where each number signifies a specific height.

## Constraints:

- Hiking trails can only move upwards (i.e., the height increases) by exactly `1` increment from the previous point (up, down, left, or right).
- Trails cannot move diagonally.
- Only consider trailheads (`0` points) that can reach `9` following the given hiking trail rules.
- It is assumed that the input grid is of a reasonable size for processing without causing memory overflow errors.

## Output:

The output should be a single integer value: the sum of scores of all trailheads present on the map.

## Hints:

Consider employing a depth-first search (DFS) or breadth-first search (BFS) algorithm for finding paths from `0` to `9`. These can be implemented utilizing recursion or iterative approaches with stacks or queues respectively.

An example in Python:
```python
def dfs(grid, i, j):
  # Check if the indices are valid and conduct the search
  pass
```
Remember to keep track of the paths you have already visited to avoid revisiting them.