from collections import deque


money = [int(el) for el in input().split()]
food_prices = deque([int(el) for el in input().split()])
food_count = 0

while money and food_prices:
    difference = money.pop() - food_prices.popleft()

    if difference == 0:
        food_count += 1
    elif difference > 0:
        food_count += 1
        if not money:
            money = [difference]
        else:
            money[-1] += difference


if food_count >= 4:
    print(f"Gluttony of the day! Henry ate {food_count} foods.")
elif 1 < food_count < 4:
    print(f"Henry ate: {food_count} foods.")
elif food_count == 1:
    print(f"Henry ate: {food_count} food.")
else:
    print(f"Henry remained hungry. He will try next weekend again.")