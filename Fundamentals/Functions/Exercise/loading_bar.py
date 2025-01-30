def loading_bar(n):
    bar = ["."] * 10
    n //= 10

    for index in range(n):
        bar[index] = "%"
    if n == 10:
        return f"100% Complete!\n[{''.join(bar)}]"
    return f'{n*10}% [{"".join(bar)}]\nStill loading...'

percentage = int(input())

print(loading_bar(percentage))

# second solution

def loading_bar(num):
    border = num // 10
    bar = ["."] * 10
    dots = bar[border:]
    percent = ["%"] * border
    bar = percent + dots

    if num == 100:
        return f'{num}% Complete!\n[{"".join(bar)}]'
    return f'{num}% [{"".join(bar)}]\nStill loading...'


number = int(input())

print(loading_bar(number))

# third solution

def loading_bar(percentage):
    num = percentage // 10
    bar = f'[{"%" * num}{"." * (10-num)}]'
    return f"{percentage}% Complete!\n{bar}" if percentage == 100 else f"{percentage}% {bar}\nStill loading..."

number = int(input())

print(loading_bar(number))
