# 1Take input from user
string = input("Enter a string: ")

# Calculate length
length = len(string)

# Display result
print("Length of the string is:", length)

#output
Enter a string: hello
Length of the string is: 5

# 2Take input from user
string = input("Enter a string: ")

# Check if string length is at least 2
if len(string) < 2:
    print("String is too short")
else:
    new_string = string[:2] + string[-2:]
    print("New string:", new_string)

    #output
Enter a string: python
New string: pyon


    # 3Take input from user
str1 = input("Enter first string: ")
str2 = input("Enter second string: ")

# Concatenate strings
result = str1 + str2

# Display result
print("Concatenated string:", result)
#output
Enter first string: Hello
Enter second string: World
Concatenated string: HelloWorld