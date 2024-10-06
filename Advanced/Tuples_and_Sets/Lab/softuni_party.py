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
