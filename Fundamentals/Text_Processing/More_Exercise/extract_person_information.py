import re


def extract_name_and_age(n, lines):
    for line in lines:
        name_match = re.search(r"@([A-Za-z]+)\|", line)
        age_match = re.search(r"#(\d+)\*", line)

        if name_match and age_match:
            name = name_match.group(1)
            age = age_match.group(1)
            print(f"{name} is {age} years old.")


n = int(input())
lines = [input() for _ in range(n)]

extract_name_and_age(n, lines)
