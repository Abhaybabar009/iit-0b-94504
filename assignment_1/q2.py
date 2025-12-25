#Q2:
#Count Even and Odd Numbers
#Take a list of numbers as input (comma-separated).
#Count how many are even and how many are odd.
#Print results.
#Example Input:
#10, 21, 4, 7, 8




# Take comma-separated input
numbers = input("Enter numbers (comma-separated): ")

# Convert input string into list of integers
num_list = [int(x) for x in numbers.split(",")]

even_count = 0
odd_count = 0

# Count even and odd numbers
for n in num_list:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

# Print results
print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
