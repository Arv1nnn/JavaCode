# JavaCode

This Java program finds the size of the largest connected island in a given 2D grid representing a nautical map.  

## How It Works:
- The map consists of:
  - `'@'` for land  
  - `'~'` for water  
- Islands are groups of adjacent land cells (only horizontal and vertical connections count).  
- Uses Breadth-First Search (BFS) to traverse islands and determine their sizes.  
- The program reads the grid from input, processes it, and returns the size of the largest island.
