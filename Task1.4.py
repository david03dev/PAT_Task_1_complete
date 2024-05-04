#Write a program to takes a string and retruns the number of unique characters in it

#get input from user
Input_string = str(input("Enter the string : "))
#make input string as upper case for manipulation
Input_string = Input_string.upper()
#initialize result as empty string
result = ""
#Logic to identify unique characters
for letter in Input_string:
    if letter not in result and letter != " ":
        result = result+letter
#print the lenght of the result(no of unique characters)
print("The number of unique characters in given string is: ",len(result))