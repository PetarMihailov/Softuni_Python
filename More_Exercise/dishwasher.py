detergent = int(input()) * 750
command = input()

counter = 0
dishes = 0
pots = 0

while not command == "End":
    counter += 1
    command = int(command)
    if counter % 3 == 0:
        pots += command
        detergent -= command * 15
    else:
        dishes += command
        detergent -= command * 5

    if detergent < 0:
        break
        
    command = input()

if detergent >= 0:
    print(f"Detergent was enough!\n{dishes} dishes and {pots} pots were washed.\nLeftover detergent {detergent} ml.")
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")
