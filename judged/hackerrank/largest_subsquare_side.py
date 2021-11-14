
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
