# Program to print a diamond star pattern

# First half: Print the upper pyramid
for i in range(1, 6):

    # Print spaces before stars to align the pattern
    for j in range(5 - i):
        print("  ", end="")

    # Print odd number of stars in increasing order
    for k in range(2 * i - 1):
        print("*", end=" ")

    # Move to the next line
    print()

# Second half: Print the lower inverted pyramid
for i in range(4, 0, -1):

    # Print spaces before stars
    for j in range(5 - i):
        print("  ", end="")

    # Print odd number of stars in decreasing order
    for k in range(2 * i - 1):
        print("*", end=" ")

    # Move to the next line
    print()