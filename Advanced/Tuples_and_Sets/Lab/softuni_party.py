n = int(input())

reservations = set()

for _ in range(n):
    reservations.add(input())

guests = input()

arrived = set()

while not guests == "END":
    arrived.add(guests)

    guests = input()

print(len(reservations - arrived))

for el in sorted(reservations.difference(arrived)):
    if el[0].isdigit():
        print(el)

for el in sorted(reservations.difference(arrived)):
    if el[0].isalpha():
        print(el)

# second solution

reservations = set([input() for _ in range(int(input()))])

guest = input()

while not guest == "END":
    reservations.discard(guest)

    guest = input()

print(len(reservations))

[print(el) for el in sorted(reservations)]
