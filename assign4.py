#write a  code to diplay even numbers from 1to 10                                    
for i in range(1, 11):
    if i % 2 == 0:
        print(i)

 #write a code to add odd numers from 1 to 10  
 sum = 0

for i in range(1, 11):
    if i % 2 != 0:
        sum += i

print("Sum of odd numbers:", sum)
# output
Sum of odd numbers: 25

# wap to get the fibonacci series between 0 to 50
a, b = 0, 1

print("Fibonacci series from 0 to 50:")

while a <= 50:
    print(a, end=" ")
    a, b = b, a + b

    #output
    0 1 1 2 3 5 8 13 21 34

    # wap to remove the charecteristics which have odd index values of a given string
    string = input("Enter a string: ")

result = ""

for i in range(len(string)):
    if i % 2 == 0:   # keep even index characters
        result += string[i]

print("Result:", result)

#output
Input:  hello
Output: hlo
