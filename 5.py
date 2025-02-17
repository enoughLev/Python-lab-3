strings = int(input())
unique_words = set()

while strings > 0:
    text_string = input().split()
    unique_words.update(set(text_string))

    strings -= 1

print(f"Unique words: {len(unique_words)}")
