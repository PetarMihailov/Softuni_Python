def process_input(data_type, value):
    result = None
    if data_type == "int":
        result = f"{int(value) * 2:.0f}"
    elif data_type == "real":
        result = f"{float(value) * 1.5:.2f}"
    elif data_type == "string":
         result = f"${value}$"
    return result


data_type = input()
value = input()
print(process_input(data_type, value))
