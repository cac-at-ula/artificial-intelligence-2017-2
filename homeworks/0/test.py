from MazeUtils import MazeUtils
from Maze import TkDrawer

filename = 'test_maze.txt'

# file to numpy
mu = MazeUtils()
np_maze = mu.maze_to_numpy(filename)

# Show maze
TkDrawer(np_maze.transpose())

