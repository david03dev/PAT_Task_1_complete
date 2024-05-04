#write a program that takes two strings and returns a longest common substring between them

String_1 = str(input("Enter the first string : "))
String_2 = str(input("Enter the 2nd string : "))

#find the length of the input string
len_s1 = len(String_1)
len_s2 = len(String_2)


result = 0
for i in range(len(String_1)):
    for j in range(len(String_2)):
        k = 0
        while ((i + k) < len(String_1) and (j + k) < len(String_2)
            and String_1[i + k] == String_2[j + k]):
                k = k + 1
        result = max(result, k)

print(result)
