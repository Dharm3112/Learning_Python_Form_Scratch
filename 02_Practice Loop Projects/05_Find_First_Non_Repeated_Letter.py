input_string = input("Enter a string: ")

for char in input_string:
    print(char)
    if input_string.count(char) == 1:
        print("Char Is : ",char)
        break