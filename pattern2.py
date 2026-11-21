# Program to print a right-angled triangle star pattern

# Outer loop controls the number of rows
for i in range(1, 6):

    # Inner loop prints stars according to the row number
    for j in range(i):

        # Print star with a space on the same line
        print("*", end=" ")

    # Move to the next line after printing stars in each row
    print()