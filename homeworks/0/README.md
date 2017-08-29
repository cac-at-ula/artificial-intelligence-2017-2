# Homework #0

- Due: Tuesday 5, September, 2017

## Description

The first homework consist in reading a maze description from a file, and convert it to a numpy representation.

For example, is the file contains

```
1111
1001
1111
```

Then the resulting numpy array is

```python
np.array([[1,1,1,1],[1,0,0,1],[1,1,1,1]])
```

## Instructions

Fill the method maze\_to\_numpy from MazeUtils

```python
def maze_to_numpy(self, filename):
    """ Reads a file that contains the description of a maze. Returns a numpy
    representation of the mze
    
    :filename: filename that constains the description of the maze
    :returns: Numpy array

    """

    #
    # Add code here
    #
    pass
    #
    # End code

```


## Tips

1. Check the method **open**
2. Remember that files contains text, and you need numbers
3. Test the code.

```
python3 test.py
```

## Evaluation

1. 6 if the method works
2. 7 if 1 works, it has a clear code and good comments
3. 1, otherwise

## Submission

1. Submissions are through Platea.
2. Submission must include just the file MazeUtils.py compressed as a zip file
3. The zip file must be named homework_0_rut.zip . Rut in the format XXXXXXXX-X







