#write a program that takes a string and returns the number of words in it

input_string = str(input("Enter the string: "))

result = 0
#remove unwanted white spaces from input string
input_string = input_string.strip()


#count the spaces to calculate number of words
for i in range(len(input_string)):
    if input_string[i] == " " and input_string[i-1] != " " and i > 0:
        result += 1

#increment by 1 for last word count
print ("Number of words in the input string is ",result+1)
