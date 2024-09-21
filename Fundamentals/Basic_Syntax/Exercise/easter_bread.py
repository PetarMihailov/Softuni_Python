budget = float(input())
flour = float(input())
eggs = flour * 0.75
milk = flour * 1.25 / 4
loaf = eggs + flour + milk

colored_eggs = 0
loaves = 0

while budget >= loaf:
    colored_eggs += 3
    loaves += 1
    budget -= loaf

    if loaves % 3 == 0:
        colored_eggs -= loaves - 2

print(f"You made {loaves} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
