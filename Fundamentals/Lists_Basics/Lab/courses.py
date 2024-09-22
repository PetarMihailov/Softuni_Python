n = int(input())

courses = []

for _ in range(n):
    course = input()
    courses.append(course)

print(courses)

# second solution

n = int(input())

courses = [input() for _ in range(n)]

print(courses)
