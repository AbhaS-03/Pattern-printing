# Program to print a butterfly star pattern

# First half: Print the upper part of the butterfly
for i in range(1, 6):

    # Print increasing stars on the left side
    for j in range(i):
        print("*", end=" ")

    # Print spaces in the middle
    for j in range(2 * (5 - i)):
        print("  ", end="")

    # Print increasing stars on the right side
    for j in range(i):
        print("*", end=" ")

    # Move to the next line
    print()


# Second half: Print the lower part of the butterfly
for i in range(4, 0, -1):

    # Print decreasing stars on the left side
    for j in range(i):
        print("*", end=" ")

    # Print increasing spaces in the middle
    for j in range(2 * (5 - i)):
        print("  ", end="")

    # Print decreasing stars on the right side
    for j in range(i):
        print("*", end=" ")

    # Move to the next line
    print()