import re

def process_orders():
    total_income = 0

    while True:
        line = input()
        if line == "end of shift":
            break

        pattern = r"%(?P<customer>[A-Z][a-z]+)%.*?<(?P<product>\w+)>.*?\|(?P<count>\d+)\|.*?(?P<price>\d+(\.\d+)?)\$"
        match = re.match(pattern, line)

        if match:
            customer = match.group("customer")
            product = match.group("product")
            count = int(match.group("count"))
            price = float(match.group("price"))

            total_price = count * price
            total_income += total_price

            print(f"{customer}: {product} - {total_price:.2f}")
            
    print(f"Total income: {total_income:.2f}")


process_orders()
