#wap to create a list and demonstrate membership operators (in,not in ) to check element presence 
# Create a list
my_list = [10, 20, 30, 40, 50]

# Take input from user
element = int(input("Enter an element to check: "))

# Check using 'in'
if element in my_list:
    print(element, "is present in the list")
else:
    print(element, "is NOT present in the list")

# Check using 'not in'
if element not in my_list:
    print(element, "is not in the list")
else:
    print(element, "is in the list")

# output
Enter an element to check: 30
30 is present in the list
30 is in the list

# Create a list
my_list = [10, 20, 30, 40, 50, 60]

print("List:", my_list)

# Indexing (positive indexing)
print("Element at index 0:", my_list[0])
print("Element at index 2:", my_list[2])

# Negative indexing
print("Element at index -1 (last element):", my_list[-1])
print("Element at index -3:", my_list[-3])

# Slicing
print("Elements from index 1 to 4:", my_list[1:5])
print("Elements from start to index 3:", my_list[:4])
print("Elements from index 2 to end:", my_list[2:])
print("Entire list:", my_list[:])
print("Every second element:", my_list[::2])

List: [10, 20, 30, 40, 50, 60]
Element at index 0: 10
Element at index 2: 30
Element at index -1 (last element): 60
Element at index -3: 40
Elements from index 1 to 4: [20, 30, 40, 50]
Elements from start to index 3: [10, 20, 30, 40]
Elements from index 2 to end: [30, 40, 50, 60]
Entire list: [10, 20, 30, 40, 50, 60]
Every second element: [10, 30, 50]

# Create a list
my_list = [10, 20, 30, 40, 50]

print("Original List:", my_list)

# Update element (change value at a specific index)
my_list[2] = 35
print("After updating index 2:", my_list)

# Append element (add at end)
my_list.append(60)
print("After appending 60:", my_list)

# Insert element (add at specific position)
my_list.insert(1, 15)
print("After inserting 15 at index 1:", my_list)

# Delete element using remove() (removes first occurrence)
my_list.remove(40)
print("After removing 40:", my_list)

# Delete element using pop() (removes by index)
my_list.pop(3)
print("After popping element at index 3:", my_list)

# Delete entire list elements
my_list.clear()
print("After clearing list:", my_list)

#output
Original List: [10, 20, 30, 40, 50]
After updating index 2: [10, 20, 35, 40, 50]
After appending 60: [10, 20, 35, 40, 50, 60]
After inserting 15 at index 1: [10, 15, 20, 35, 40, 50, 60]
After removing 40: [10, 15, 20, 35, 50, 60]
After popping element at index 3: [10, 15, 20, 50, 60]
After clearing list: []

# Create two lists
list1 = [10, 20, 30]
list2 = [40, 50, 60]

print("List 1:", list1)
print("List 2:", list2)

# Concatenation
concat_list = list1 + list2
print("After concatenation:", concat_list)

# Repetition
repeat_list = list1 * 2
print("After repetition:", repeat_list)

# Length
print("Length of list1:", len(list1))

# Maximum element
print("Maximum in list2:", max(list2))

# Minimum element
print("Minimum in list2:", min(list2))

#output

List 1: [10, 20, 30]
List 2: [40, 50, 60]
After concatenation: [10, 20, 30, 40, 50, 60]
After repetition: [10, 20, 30, 10, 20, 30]
Length of list1: 3
Maximum in list2: 60
Minimum in list2: 40