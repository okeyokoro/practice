"""
LARGEST SUB-SQUARE SIDE
=======================

As a game developer, you need to analyze the various worlds that have been
designed. Each world is modeled as a 2-dimensional square grid where each 
cell contains an integer value. 

A grid can be divided into `square`  subgrids that 
have rows and columns ≤ the number of rows and columns in the original grid.
For each subgrid, all of its elements are summed to get a `total value`
for the subgrid. A fellow analyst provides an integer and wants to know the maximum
number of rows or columns of the square subgrids such that all of the subgrids
of that size have a total value less than that integer.

As an example, a `grid` and all its subgrids are shown below:

Grid:

2 2 2
3 3 3
4 4 4

Square subgrids:

rows/columns = 1

2, 2, 2, 3, 3, 3, 4, 4, 4
maximum sum = 4

rows/columns = 2

2 2	2 2	3 3	3 3
3 3	3 3	4 4	4 4
maximum sum = 14

rows/columns = 3

2 2 2
3 3 3
4 4 4
maximum sum = 27

If the desired maximum total value k is ≥ 27, the entire grid satisfies the condition
so answer = 3. If 14 ≤ k < 27, answer = 2. If 4 ≤ k < 14, answer = 1. 
Finally, if k < 4 there is no subgrid satisfies the condition, 
so answer = 0.

"""

def largestSubsquareSide(grid, k):
    # input is square, output is square rows = columns
    # Here is an example sub-grid dimension (<= rows_of_grid, <= columns_of_grid )
    # The goal is to find the largest sub-grid dimension such that ANY subgrid of that dimension
    # contains elements that when summed; have a value less than k

    # start from the largest possible square grid
    grid_dim = len(grid)
    dimension = grid_dim

    def subgrid_sum(dimension, grid, row, col):
        """ Given an element of grid[row][col]
        find all the elements needed to form a subgrid

        (lets treat the current element as the top-left element,
         <then add the remaining columns needed from that row>,
         go to the next row,
         <then add the columns needed from that row>
         then go to the required c)

        and add them up
        """
        count = 0
        for r in range(row, row+dimension):
            for c in range(col, col+dimension):
                try:
                    count += grid[r][c]
                except IndexError:
                    # if there is an IndexError then this is element cannot form a subgrid
                    return 0
        return count

    while dimension > 0:
        # generate a list containing the sum of items in a subgrid; for all subgrids; for a given dimension
        subgrid_sums = []
        
        # do a search in the number of directions needed. per elements
        # if dimension is 1; then no search
        # if dimension is 2; then 2**2 - 1 other elements to add to subgrids
        # if dimension is 3; then 3**3 -1 other elements to add to subgrid
        for row in range(grid_dim):
            for col in range(grid_dim):
                subgrid = subgrid_sum(dimension, grid, row, col)
                subgrid_sums.append(subgrid)
        
        # if max(list of sums) is not greater than k; not max(list_of_sums) > k; return k
        if not max(subgrid_sums) > k:
            return dimension
        
        dimension -= 1

    return 0