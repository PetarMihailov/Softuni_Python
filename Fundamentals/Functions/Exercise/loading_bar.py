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
