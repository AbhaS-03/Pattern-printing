# Program to print an inverted right-angled triangle pattern

# Outer loop controls the number of rows
for i in range(5, 0, -1):

    # Inner loop prints stars according to the current row number
    for j in range(i):

        # Print star with a space on the same line
        print("*", end=" ")

    # Move to the next line after printing stars in each row
    print()