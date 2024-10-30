name = input("What is your name? ")
print("Hello,", name)

fruits = []

# Error handling for user input on the number of fruits
while True:
    try:
        num_fruits = int(input("(Shopping List)How many fruits would you like to add? "))
        if num_fruits < 1:
            print("Please enter a positive number.")
        else:
            break  # Exit the loop if a valid number is entered
    except ValueError:
        print("Invalid input. Please enter a whole number.")

# Loop based on the specified number of fruits
for index in range(num_fruits):
    fruit = input(f'Please enter fruit number {index + 1}: ')
    fruits.append(fruit)

# Define the filename
filename = "fruits_list.txt"

# Write the list of fruits to a text file
with open(filename, "w") as file:
    file.write("The list of fruits you entered:\n")
    for i, fruit in enumerate(fruits, start=1):
        file.write(f"{i}. {fruit}\n")

print(f"\nThe list has been saved to {filename}")



print('Thank You')













