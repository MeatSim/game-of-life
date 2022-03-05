# Conway's Game of Life
Coded in Python as a *Head First Learn to Code* project. The MVC (Model View Controller) pattern separates the user interface from the code used to compute future generations. The GUI (graphical user interface) is built using the `Tkinter` module.
## What is Life?
~~42. No, wait, that's the *meaning* of life.~~ [Conway's Game of Life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) simulates cells that live or die according to four simple rules:
1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
2. Any live cell with two or three live neighbours lives on to the next generation.
3. Any live cell with more than three live neighbours dies, as if by overpopulation.
4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
These simple rules can create complex patterns as each generation progresses. "Live" cells are represented by black pixels, which turn white when they "die."
## How to play
1. Either choose a pattern (glider, glider gun, or random) with the Choose a Pattern button or draw cells directly onto the grid.
2. Press Start to start generating new generations.
3. Press Pause to pause.
4. Press Clear to clear the grid.
## Setup
1. Make sure you have [Python](https://www.python.org/downloads/) installed.
2. Clone the repository to your computer.
3. Start IDLE.
4. Open view.py (File > Open or Ctrl+O).
5. In the view.py window, run the module (Run > Run Module or F5).
## Torus feature
The original grid ended at the edges. The torus feature causes each edge to wrap around to the other side. The right edge connects to the left edge, and the bottom edge connects to the top edge. 
