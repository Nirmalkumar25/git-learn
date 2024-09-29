"""
Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function
"""

max_num = int(input("Enter a max number: "))
odd_numbers = [i for i in range(max_num+1) if i%2 == 1]
print(f"Odd numbers between 1 and {max_num}: ", odd_numbers)

