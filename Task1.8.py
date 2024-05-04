#write a program that takes a string and returns True if it is anagram of another string, False otherwise

#get input from user
input_str1 = str(input("Enter the first string: "))
input_str2 = str(input("Enter the 2nd string: "))
#remove unwanted white spaces
input_str1 = input_str1.strip()
input_str2 = input_str2.strip()
#initialize result with string date
result = ""

#check if two string equal in length
if len(input_str1) != len(input_str2):
    print("Entered strings are not a anagram")
#check each letter count in both string
else:
    for letter in input_str1:
        count_1 = 0
        count_2 = 0
        for i in range(len(input_str1)):
            if letter == input_str1[i]:
                count_1 = count_1 + 1
            if letter == input_str2[i]:
                count_2 = count_2 + 1
        if count_1 != count_2:
            result = result + "No"    
    #Print the results
    if "No" in result:
        print("Given strings are not anagram")
    else:
        print("Given are anagram strings")