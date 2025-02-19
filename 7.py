string = "text test text apple new_task python love love 1 1 00 0 1 02"
spis = string.split()

word_count = {}

for word in spis:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("\nOutput:")
for key, value in word_count.items():
    print(f"{key}: {value}")

#print(word_count)