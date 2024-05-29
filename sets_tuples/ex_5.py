n = int(input())

reservations = set()

for _ in range(n):
    guest_num = input()
    reservations.add(guest_num)

reservation_number = input()

while reservation_number != "END":
    if reservation_number in reservations:
        reservations.remove(reservation_number)
    reservation_number = input()

print(len(reservations))

sorted_reservations = sorted(reservations)
for reservation in sorted_reservations:
    print(reservation)