# Search Algorithms Module in AI

## Description

This is a class-based module based on various graph search algorithms:
- <ins>Uninformed</ins> (don't have information about the state, or search space, other than how to traverse it)
  - Breadth-First Search (BFS)
  - Bidirectional Search
  - Depth-First Search (DFS)
  - Depth-Limited Search
  - Iterative deepening DFS
  - Uniform Cost Search (UCS)
- <ins>Informed</ins> (uses the idea of a heuristic to improve the search. A heuristic function takes the current state as input and gives a value of how close it is to the search goal)
  - Best-First Search (Greedy)
  - Astar (A*)
- <ins>Local</ins> (it is based on the optimization of the current state and it will stop if the following states are not better. This doesn't mean that the search had found the best solution)
  - Hill Climbing
  - Simulated Annealing

## Tools and technologies learned

- classes in Python
- modules in Python
- various search algorithms

## Installation and run

Simply clone the repo, prepare your Python environment (math, heapq and random libraries were used, so most modern Python versions 
should work). This is only temporary until the publish of the module (then you may use package manager such as pip).

Example using Anaconda -> Open cmd terminal and type:
```
conda create --name *yourEnvironmentName* python=3.10

cd *pathToFolderWhereYouClonedIt*

activate yourEnvironmentName

python main.py
```

If it takes too long and you want to stop the process, in the same terminal, use CTRL+D key combination.

If you want to deactivate the conda environment, in the terminal type:
```
conda deactivate *yourEnvironmentName*
```

## Visuals

### Test Graph
![SSTestGraph](screenshots%2FSSTestGraph.png)

### Depth First Search
![SSDepthFirstInput](screenshots%2FSSDepthFirstInput.png)
![SSDepthFirstResult](screenshots%2FSSDepthFirstResult.png)

### Breadth First Search
![SSBreadthFirstInput](screenshots%2FSSBreadthFirstInput.png)
![SSBreadthFirstResult](screenshots%2FSSBreadthFirstResult.png)

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Feel free to contact me at: karjhan1999@gmail.com