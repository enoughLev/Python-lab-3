strings = int(input())
synonimous = dict()

while strings > 0:
    strings -= 1
    inp = input().split()
    synonimous[inp[0]] = inp[1]

syn = input()
print("\nOutput:")
for key, value in synonimous.items():
    if value == syn:
        print(key)
    elif key == syn:
        print(synonimous[syn])
