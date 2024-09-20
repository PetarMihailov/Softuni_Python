def data_types(command, content):
    if command == "int":
        result = int(content) * 2
        return result
    elif command == "real":
        result = f"{(float(content) * 1.5):.2f}"
        return result
    elif command == "string":
        result = f"${content}$"
        return result


data_1 = input()
data_2 = input()
total = data_types(data_1, data_2)
print(total)
