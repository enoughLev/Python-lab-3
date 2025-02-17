sets = set()

numbers = input().split()
doubles = set()

for number in numbers:
    if number in doubles:
        print(f"{number} - YES")
    else:
        print(f"{number} - NO")
        doubles.add(number)