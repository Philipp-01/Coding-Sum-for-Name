name = input("Enter your name:")
numbers = []
new_name = ''.join(filter(str.isalnum, name))
normal_str1 = new_name
lower_str1 = normal_str1.lower()
for letter in lower_str1:
    number = ord(letter) -96
    numbers.append(number)
    NameSum = sum(numbers)
print('The value of your name is', NameSum)