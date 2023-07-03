import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

password_length = int(input("Enter the desired password length: "))
random_password = generate_random_password(password_length)

print("Your random password is:", random_password)




numbers = []
count = int(input("Enter the number of elements: "))  # Prompt the user to enter the number of elements

for i in range(count):
    num = float(input("Enter number {}: ".format(i+1)))  # Prompt the user to enter each number
    numbers.append(num)  # Add the number to the list

max_num = max(numbers)  # Find the maximum number
min_num = min(numbers)  # Find the minimum number

print("Maximum number:", max_num)
print("Minimum number:", min_num)
