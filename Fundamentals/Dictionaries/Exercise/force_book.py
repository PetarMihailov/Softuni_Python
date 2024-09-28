data = input()

forces = {}

while not data == "Lumpawaroo":
    if "|" in data:
        side, user = data.split(" | ")
        check = False
        for key, value in forces.items():
            if user in value:
                check = True
                break
        if not check and side not in forces:
            forces[side] = [user]
        elif not check and side in forces:
            forces[side].append(user)
    elif "->" in data:
        user, side = data.split(" -> ")
        for key, value in forces.items():
            if user in value:
                value.remove(user)
                break
        if side not in forces:
            forces[side] = [user]
        elif side in forces and user not in forces[side]:
            forces[side].append(user)


        print(f"{user} joins the {side} side!")

    data = input()

for key in forces:
    if forces[key]:
        print(f"Side: {key}, Members: {len(forces[key])}")
    for user in forces[key]:
        print(f"! {user}")
