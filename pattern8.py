# Program to print an inverted pyramid star pattern

# Outer loop controls the number of rows
for i in range(5, 0, -1):

    # Print spaces before stars to shift the pattern towards the right
    for j in range(5 - i):
        print("  ", end="")

    # Print odd number of stars in decreasing order
    for k in range(2 * i - 1):
        print("*", end=" ")

    # Move to the next line after printing each row
    print()