#input
input_string = input("Enter a string: ")

#remove spaces and convert to lowercase for a case-insensitive comparison
string = input_string.replace(" ", "").lower()

#initialize a flag variable
is_palindrome = True

#loop through the string
for index in range(len(string) // 2):
    if string[index] != string[-(index + 1)]:
        is_palindrome = False
        break

#check the flag variable to determine if the string is a palindrome
if is_palindrome:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")