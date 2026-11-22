# Program to print a number triangle pattern

# Outer loop controls the number of rows
for i in range(1, 6):

    # Inner loop prints numbers from 1 to the current row number
    for j in range(1, i + 1):

        # Print the number with a space on the same line
        print(j, end=" ")

    # Move to the next line after printing numbers in each row
    print()