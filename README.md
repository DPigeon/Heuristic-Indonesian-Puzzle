# Heuristic Indonesian Dot Puzzle

First, install Miniconda with Python 3.7 at

```
https://docs.conda.io/en/latest/miniconda.html
```

You also need NumPy to run the project.

Install NumPy with

```
conda install numpy
```

# Before Running

To run the project, make sure you have some input inside the /input folder.
Inputs can be boards of 3x3 to 10x10 boards. The format is:

```
size maxDepthSearch maxSearchPathLength boardValues
```

For example:

```
4 9 50 1110010110111010
3 100 200 101010100
```

For the example above, the first input on line one would look like this:

```
  1 2 3 4
A 1 1 1 0
B 0 1 0 1
C 1 0 1 1
D 1 0 1 0
```

Where a 0 is a white token and a 1 is a gray token. The goal is to have all white tokens on the board such as this 4x4:

```
  1 2 3 4
A 0 0 0 0
B 0 0 0 0
C 0 0 0 0
D 0 0 0 0
```

# Run

On the root of the project, enter

```
python Puzzle.py
```

# Outputs

The outputs are located in the /output folder.
There are 2 types of output files: solution and search.

Search Format:

```
f(n) g(n) h(n) valuesOfNodes
```

Example:

```
0 0 0 1010010111001010
0 0 0 0010100101001010
```

Solution Format:

```
touchMove resultingBoardValues
```

Example:

```
0 1010010111001010
B1 0010100101001010
```
