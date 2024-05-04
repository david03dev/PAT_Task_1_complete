#Create a pyramid of numbers from 1 to 20 using for loop?

total_rows = 20  # Number of rows in the pyramid


for row in range(1, total_rows + 1):
    #loop for print leading spaces
    for space in range(total_rows-row):
        print(" ",end="")
    #loop for print first half row of numbers
    for number in range(1,row):
        print(number,end="")
    #loop for print next half row of numbers
    for row in range(row,0,-1):
        print(row,end="")

    # print new line
    print("\n")
