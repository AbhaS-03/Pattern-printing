# Program to print a right-aligned triangle star pattern

# Outer loop controls the number of rows
for i in range(1, 6):

    # Print spaces before stars to align the pattern to the right
    for j in range(5 - i):
        print("  ", end="")

    # Print stars according to the current row number
    for k in range(i):
        print("*", end=" ")

    # Move to the next line after printing each row
    print()