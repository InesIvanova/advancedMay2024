from collections import deque

kids = deque(input().split())
n = int(input()) - 1
turns = 0

while len(kids) > 1:
    kids.rotate(-n)
    print(f"Removed {kids.popleft()}")

    # for i in range(n-1):
    #     # Get first kid on the line
    #     first_kid = kids.popleft()
    #     # Move the kid in the end
    #     kids.append(first_kid)

print(f"Last is {kids.popleft()}")