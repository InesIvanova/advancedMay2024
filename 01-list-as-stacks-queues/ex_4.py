from collections import deque

liters = int(input())
queue = deque([])

name = input()

while name != "Start":
    queue.append(name)
    name = input()

command = input()

while command != "End":
    if command.isdigit():
        liters_wanted = int(command)
        person = queue.popleft()

        if liters >= liters_wanted:
            print(f"{person} got water")
            liters -= liters_wanted
        else:
            print(f"{person} must wait")
    else:
        _, liters_to_refill = command.split()
        liters_to_refill = int(liters_to_refill)
        liters += liters_to_refill

    command = input()

print(f"{liters} liters left")