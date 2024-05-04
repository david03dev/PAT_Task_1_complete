#write a program that takes a string and returns the most frequent character in it

#get input from user
input_string = str(input("Enter the string: "))
input_string = input_string.upper()
result = 0
letter_count = 0

#calculate the frequency of the each characters in sting
for letter in input_string:
    counter = 0
    for i in range(len(input_string)):
        if letter == input_string[i]:
            counter = counter + 1
    if counter > letter_count:
        letter_count = counter
        result = letter

#print the results
print("Most frequent character in given string is : ",result)
print("Frequency of the character """,result, " is ", letter_count)