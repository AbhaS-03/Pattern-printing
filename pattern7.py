# Program to print a pyramid star pattern

# Outer loop controls the number of rows
for i in range(1, 6):

    # Print spaces before stars to align the pattern
    for j in range(5 - i):
        print("  ", end="")

    # Print odd number of stars in each row
    for k in range(2 * i - 1):
        print("*", end=" ")

    # Move to the next line after printing each row
    print()