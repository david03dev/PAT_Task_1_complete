#Write a program that takes a string and returns the new string with all the vowels removed?

#get input from user
input_string = str(input("Enter the string: "))
result = ""

#logic to check and remove the vowel letters from input string
for letter in input_string:
    if letter.upper() not in "AEIOU":
        result = result + letter

print("The string with removed vowels is :",result)