def calculations(operator, num_1, num_2):
    result = None

    if operator == 'add':
        result = num_1 + num_2
    elif operator == 'subtract':
        result = num_1 - num_2
    elif operator == 'multiply':
        result = num_1 * num_2
    elif operator == 'divide':
        result = num_1 // num_2

    return result

print(calculations(input(), int(input()), int(input())))
