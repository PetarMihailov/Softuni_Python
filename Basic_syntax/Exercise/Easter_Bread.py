budget = float(input())
flour = float(input())

eggs = flour * 0.75
milk = flour * 1.25 / 4
colored_eggs = 0
current_count = 0
price_bread = eggs + flour + milk


while budget > price_bread:
    current_count += 1
    colored_eggs += 3
    budget -= price_bread

    if current_count % 3 == 0:
        colored_eggs -= current_count - 2

print(f'You made {current_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.')

