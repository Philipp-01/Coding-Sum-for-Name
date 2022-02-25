name = input("Enter your name:")
numbers = []
new_name = ""
for character in name:
    if character.isalnum():
        new_name += character
normal_str1 = new_name
lower_str1 = normal_str1.lower()
for letter in lower_str1:
    number = ord(letter) -96
    numbers.append(number)
numbersum = sum(numbers)
print('The value of your name is', numbersum)