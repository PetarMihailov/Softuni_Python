def take_skip_rope(message):
    # Split the string into numbers and non-numbers
    numbers = [int(ch) for ch in message if ch.isdigit()]
    non_numbers = [ch for ch in message if not ch.isdigit()]

    # Separate the numbers into take and skip lists
    take_list = numbers[::2]
    skip_list = numbers[1::2]

    # Iterate over take and skip lists to build the result
    result = []
    index = 0

    for take, skip in zip(take_list, skip_list):
        # Take 'take' characters
        result.extend(non_numbers[index:index + take])
        # Update the index to skip 'skip' characters
        index += take + skip

    return ''.join(result)


message = input()
hidden_message = take_skip_rope(message)
print(hidden_message)  
