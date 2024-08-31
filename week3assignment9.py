#input
character = input("Enter a single character: ")

#processing
if len(character) == 1 and character.isalpha():
    character = character.lower()
    if character in 'aeiou':
        print("The character is a vowel")
    else:
        print("The character is a consonant")
else:
    if len(character) != 1:
        print("Error: Please enter only one character")
    else:
        print("Error: The input is not a letter")