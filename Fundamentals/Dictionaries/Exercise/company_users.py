data = input()

companies = {}

while not data == "End":
    company, _id = data.split(" -> ")
    if company not in companies:
        companies[company] = []
    if _id not in companies[company]:
        companies[company].append(_id)

    data = input()

for company in companies:
    print(company)
    for _id in companies[company]:
        print(f"-- {_id}")
