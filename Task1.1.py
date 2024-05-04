"""
write a python program to calculate the total number of vowels and count each and individual vowel
A,E,I,O,U in the string "Guvi Geeks Network Private Limited" ?
"""
Given_string = "Guvi Geeks Network Private Limited"
vowels = "AEIOU"
total_vowels = 0
Individual_count = 0

#make given string to upper case for convenience
Given_string = Given_string.upper()
print("Given string is ",Given_string)

#calculate total vowels in given string
for letter in Given_string:
    if letter in vowels:
        total_vowels = total_vowels +1
#print total vowels
print("Number of vowels in given string is ",total_vowels)

#calculate count of individual vowels from given string
for letter in vowels:
    for i in Given_string:
        if i == letter:
            Individual_count = Individual_count + 1
    #print the count of each and individual vowels
    print("Number of",letter, "in given string", Individual_count)
    Individual_count = 0