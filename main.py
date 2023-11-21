import copy
from prettytable import PrettyTable


# A function to solve the transportation problem using North-West corner method
def north_west_corner_method(grid, supply, demand):
    # Initialize the starting row and column indices
    startR, startC = 0, 0

    # Initialize the initial solution matrix with zeros
    initial_solution = [[0] * len(grid[0]) for _ in range(len(grid))]

    # Iterate through the grid until either all rows or all columns are processed
    while startR < len(grid) and startC < len(grid[0]):
        # Check if the supply in the current row is less than or equal to the demand in the current column
        if supply[startR] <= demand[startC]:
            # Assign the minimum of supply and demand to the current cell in the solution matrix
            initial_solution[startR][startC] = supply[startR]

            # Update the demand in the current column and move to the next row
            demand[startC] -= supply[startR]
            startR += 1
        else:
            # Assign the minimum of supply and demand to the current cell in the solution matrix
            initial_solution[startR][startC] = demand[startC]

            # Update the supply in the current row and move to the next column
            supply[startR] -= demand[startC]
            startC += 1

    # Return the initial solution matrix
    return initial_solution


# A function to solve the transportation problem using Vogel's approximation problem
def vogel_approximation_method(grid, supply, demand):
    # Initialize the INF
    INF = 10 ** 10

    # Initialize the sizes
    n = len(grid)
    m = len(grid[0])

    # Initialize the initial solution matrix with zeros
    initial_solution = [[0] * len(grid[0]) for _ in range(len(grid))]

    def find_diff(grid):
        # Calculate the difference between the two smallest costs in each row and column
        row_diff = [sorted(row)[1] - sorted(row)[0] for row in grid]
        col_diff = [sorted([grid[i][col] for i in range(n)])[1] - sorted([grid[i][col] for i in range(n)])[0] for col in
                    range(m)]
        return row_diff, col_diff

    # While there is still supply or demand to be satisfied
    while max(supply) != 0 or max(demand) != 0:
        # Find the differences for each row and column
        row_diff, col_diff = find_diff(grid)
        maxi1 = max(row_diff)
        maxi2 = max(col_diff)

        # If the maximum difference in rows is greater or equal to the maximum difference in columns
        if maxi1 >= maxi2:
            # Find the row with the maximum difference
            for ind, val in enumerate(row_diff):
                if val == maxi1:
                    # Find the minimum cost in that row
                    mini1 = min(grid[ind])
                    # Find the column index of the minimum cost
                    for ind2, val2 in enumerate(grid[ind]):
                        if val2 == mini1:
                            # Find the minimum between supply and demand for that cell
                            mini2 = min(supply[ind], demand[ind2])
                            # Update supply and demand
                            supply[ind] -= mini2
                            demand[ind2] -= mini2
                            # Update the initial solution matrix
                            initial_solution[ind][ind2] = mini2
                            # If demand is satisfied, mark the column with INF costs
                            if demand[ind2] == 0:
                                for r in range(n):
                                    grid[r][ind2] = INF
                            else:
                                # If not, mark the row with INF costs
                                grid[ind] = [INF for _ in range(m)]
                            break
                    break
        else:
            # If the maximum difference in columns is greater
            for ind, val in enumerate(col_diff):
                if val == maxi2:
                    # Find the minimum cost in that column
                    mini1 = INF
                    for j in range(n):
                        mini1 = min(mini1, grid[j][ind])

                    # Find the row index of the minimum cost
                    for ind2 in range(n):
                        val2 = grid[ind2][ind]
                        if val2 == mini1:
                            # Find the minimum between supply and demand for that cell
                            mini2 = min(supply[ind2], demand[ind])
                            # Update supply and demand
                            supply[ind2] -= mini2
                            demand[ind] -= mini2
                            # Update the initial solution matrix
                            initial_solution[ind2][ind] = mini2
                            # If demand is satisfied, mark the column with INF costs
                            if demand[ind] == 0:
                                for r in range(n):
                                    grid[r][ind] = INF
                            else:
                                # If not, mark the row with INF costs
                                grid[ind2] = [INF for _ in range(m)]
                            break
                    break
    # Return the initial solution matrix
    return initial_solution


# A function to solve the transportation problem using Russell's approximation problem
def russell_approximation_method(grid, supply, demand):
    # Creating a table in which the final answer will be stored
    initial_solution = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]

    # A separate function that searches for the maximum in each row and in each column
    def max_in_column_and_row():
        in_rows = [0 for _ in range(len(grid))]
        in_columns = [0 for _ in range(len(grid[0]))]

        for i in range(len(grid)):
            if supply[i] == 0:
                continue
            for j in range(len(grid[i])):
                if demand[j] == 0:
                    continue
                in_rows[i] = max(in_rows[i], grid[i][j])
                in_columns[j] = max(in_columns[j], grid[i][j])

        return in_columns, in_rows

    # A special variable that counts the number of non-zero values in the supply and demand vectors
    counter = len(grid) + len(grid[0])

    # Iterating while it is possible, that is, all possible values for supply and demand are not filled in
    while counter > 0:
        # Initialization and recalculation of each table value for the method
        new_table = copy.deepcopy(grid)
        max_in_columns, max_in_rows = max_in_column_and_row()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                new_table[i][j] -= (max_in_rows[i] + max_in_columns[j])

        # Search for the largest modulo negative value in the table
        x_coord, y_coord, value = -1, -1, 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if new_table[i][j] < value:
                    value = new_table[i][j]
                    x_coord = i
                    y_coord = j

        # Recalculation of the fill for the response and the supply and demand vectors
        if supply[x_coord] < demand[y_coord]:
            initial_solution[x_coord][y_coord] = supply[x_coord]
            demand[y_coord] -= supply[x_coord]
            supply[x_coord] = 0
        else:
            initial_solution[x_coord][y_coord] = demand[y_coord]
            supply[x_coord] -= demand[y_coord]
            demand[y_coord] = 0

        # Counting the number of non-zero values in the supply and demand vectors
        counter = 0
        for i in range(len(supply)):
            if supply[i] != 0:
                counter += 1
        for i in range(len(demand)):
            if demand[i] != 0:
                counter += 1

    # Return the initial solution matrix
    return initial_solution


# Special function for beautiful output
def print_answer(table):
    ans = PrettyTable(header=False)

    ans.add_row(["№"] + [str(i + 1) for i in range(len(table[0]))])

    for i in range(len(table)):
        ans.add_row([i + 1] + table[i])

    print(ans)


# Special function for beautiful demonstrate parameter table
def print_transportation_input(S, C, D):
    table = PrettyTable()

    # Add headers for columns
    table.field_names = [" "] + [f"D{i+1}" for i in range(len(D))]

    # Add cost matrix
    for i in range(len(C)):
        table.add_row([f"S{i+1}"] + C[i])

    # Add supply coefficients
    table.add_column("Supply", S)

    # Add demand coefficients
    table.add_row(["Demand"] + D + [" "])

    # Print the table
    print(table)


# Input data
print("Input the supply vector for your transportation problem:")
supply = list(map(int, input().split()))

print("Input the demand vector for your transportation problem")
demand = list(map(int, input().split()))

grid = [[0 for _ in range(len(demand))] for _ in range(len(supply))]
print("Input the cost table for your transportation problem:")
for i in range(len(supply)):
    grid[i] = list(map(int, input().split()))

# Checking for the applicability of the solution
for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] < 0:
            print("The method is not applicable!")
for i in supply:
    if i < 0:
        print("The method is not applicable!")
for i in demand:
    if i < 0:
        print("The method is not applicable!")

# Checking the balance of the problem
if sum(supply) != sum(demand):
    print("The problem is not balanced!")
    exit(0)

# Running all methods for the inputted data
res1 = north_west_corner_method(copy.deepcopy(grid), supply.copy(), demand.copy())
res2 = vogel_approximation_method(copy.deepcopy(grid), supply.copy(), demand.copy())
res3 = russell_approximation_method(copy.deepcopy(grid), supply.copy(), demand.copy())

# Print input parameter table
print_transportation_input(supply, grid, demand)

# Print answers for all methods
print("Answer for North-West corner method is:")
print_answer(res1)
print("Answer for Vogel's approximation method is:")
print_answer(res2)
print("Answer for Russell's approximation method is:")
print_answer(res3)
