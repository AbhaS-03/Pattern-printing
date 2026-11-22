# Program to print a hollow right-angled triangle pattern

# Outer loop controls the number of rows
for i in range(1, 6):

    # Inner loop controls the number of columns
    for j in range(1, i + 1):

        # Print stars in the first column
        # or in the last column of each row
        # or throughout the last row
        if j == 1 or j == i or i == 5:
            print("*", end=" ")

        else:
            # Print spaces inside the triangle
            print(" ", end=" ")

    # Move to the next line after each row
    print()