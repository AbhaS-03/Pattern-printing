# Program to print a repeated number triangle pattern

# Outer loop controls the number of rows
for i in range(1, 6):

    # Inner loop repeats the current row number
    for j in range(i):

        # Print the current row number with a space
        print(i, end=" ")

    # Move to the next line after printing numbers in each row
    print()