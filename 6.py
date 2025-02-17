counts = int(input())
workers = list()
unit_surname = set()
duplicate = 0

while counts > 0:
    workers.append(input())
    counts -= 1

for worker in workers:
    if worker in unit_surname:
        duplicate += 1
    else:
        unit_surname.add(worker)

print(duplicate)

