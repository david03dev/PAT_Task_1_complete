#Write a program that takes a string and returns True if it is palindrome, False otherwise

#get input from user
input_string = str(input("Enter the string : "))
input_string = input_string.upper()
Reverse_str = ""

#find a reversed string of input
for letter in input_string:
    Reverse_str = letter + Reverse_str
    
#compare input string with reversed string if matches then true, false otherwise
if Reverse_str == input_string:
    print("True: Given string is a palindrome")
else:
    print("False: Given string is not a palindrome")