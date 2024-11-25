def organize_dwarfs():
    dwarfs = {}
    hat_color_count = {}

    # Process input
    while True:
        command = input()
        if command == "Once upon a time":
            break

        name, hat_color, physics = command.split(" <:> ")
        physics = int(physics)

        # Add/update dwarf data
        if (name, hat_color) not in dwarfs:
            dwarfs[(name, hat_color)] = physics
            hat_color_count[hat_color] = hat_color_count.get(hat_color, 0) + 1
        else:
            if dwarfs[(name, hat_color)] < physics:
                dwarfs[(name, hat_color)] = physics

    # Sort dwarfs
    sorted_dwarfs = sorted(
        dwarfs.items(),
        key=lambda x: (-x[1], -hat_color_count[x[0][1]])
    )

    # Print results
    for (name, hat_color), physics in sorted_dwarfs:
        print(f"({hat_color}) {name} <-> {physics}")


# Example usage:
# Input example:
# Grumpy <:> Red <:> 100
# Dopey <:> Blue <:> 200
# Dopey <:> Red <:> 50
# Grumpy <:> Red <:> 150
# Once upon a time
organize_dwarfs()
