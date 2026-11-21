# Program to print a square star pattern

# Outer loop controls the number of rows
for i in range(4):

    # Inner loop prints 4 stars in each row
    for j in range(4):

        # Print star with a space after each star
        print("*", end=" ")

    # Move to the next line after printing 4 stars
    print()