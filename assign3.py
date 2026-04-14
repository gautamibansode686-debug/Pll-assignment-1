#program to find out greatest of 3 numbers
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

if a >= b and a >= c:
    print("Greatest number is:", a)
elif b >= a and b >= c:
    print("Greatest number is:", b)
else:
    print("Greatest number is:", c)

    #output
    Enter first number: 12
Enter second number: 45
Enter third number: 30

Greatest number is: 45
#to find odd or even number
num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")

    #output
    Enter a number: 7
    7 is odd number

    
    
   #include <stdio.h>

int main() {
    char ch;

    printf("Enter a character: ");
    scanf("%c", &ch);

    if (ch >= 'A' && ch <= 'Z') {
        printf("%c is an Uppercase letter", ch);
    }
    else if (ch >= 'a' && ch <= 'z') {
        printf("%c is a Lowercase letter", ch);
    }
    else {
        printf("%c is not an alphabet", ch);
    }

    return 0;
}

#output
Enter a character: G
G is auppercase letter




value = input("Enter something: ")

if value.isdigit():
    print("It is a Number")
elif value.isalpha():
    print("It is a Character")
else:
    print("It is a special character or mixed input")

    #output
    Enter something: 45
    it is a number