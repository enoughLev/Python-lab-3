vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}
letter = input("Введите букву русского алфавита: ")
if letter.lower() in vowels:
    print("Гласная буква")
else:
    print("Согласная буква")

if numbers in vowels: