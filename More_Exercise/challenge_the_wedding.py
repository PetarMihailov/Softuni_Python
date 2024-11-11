men_count = int(input())
women_count = int(input())
max_tables = int(input())

table_count = 0

meetings = []


for man in range(1, men_count + 1):
    for woman in range(1, women_count + 1):
        if table_count < max_tables:
            meeting = f"({man} <-> {woman})"
            meetings.append(meeting)
            table_count += 1
        else:
            break
    if table_count == max_tables:
        break

print(" ".join(meetings))
