# Program to print a hollow square star pattern

# Outer loop controls the number of rows
for i in range(5):

    # Inner loop controls the number of columns
    for j in range(5):

        # Check if it is the first or last row
        # or the first or last column
        if i == 0 or i == 4 or j == 0 or j == 4:

            # Print star on the boundary of the square
            print("*", end=" ")

        else:
            # Print spaces inside the square
            print(" ", end=" ")

    # Move to the next line after each row
    print()