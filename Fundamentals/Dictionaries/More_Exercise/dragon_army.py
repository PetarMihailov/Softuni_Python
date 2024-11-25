def dragon_stats():
    n = int(input())
    dragons = {}

    # Default stats
    DEFAULT_STATS = {"damage": 45, "health": 250, "armor": 10}

    # Process each dragon entry
    for _ in range(n):
        data = input().split()
        dragon_type, name, damage, health, armor = data
        damage = int(damage) if not damage == "null" else DEFAULT_STATS["damage"]
        health = int(health) if not health == "null" else DEFAULT_STATS["health"]
        armor = int(armor) if not armor == "null" else DEFAULT_STATS["armor"]

        if dragon_type not in dragons:
            dragons[dragon_type] = {}
        dragons[dragon_type][name] = {"damage": damage, "health": health, "armor": armor}

    # Output results
    for dragon_type, dragon_data in dragons.items():
        # Calculate averages
        total_damage = sum(dragon["damage"] for dragon in dragon_data.values())
        total_health = sum(dragon["health"] for dragon in dragon_data.values())
        total_armor = sum(dragon["armor"] for dragon in dragon_data.values())
        count = len(dragon_data)

        avg_damage = total_damage / count
        avg_health = total_health / count
        avg_armor = total_armor / count

        print(f"{dragon_type}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

        # Sort and print dragons by name
        for name, stats in sorted(dragon_data.items()):
            print(
                f"-{name} -> damage: {stats['damage']}, health: {stats['health']}, armor: {stats['armor']}"
            )


# Example usage:
# Input example:
# 5
# Red Dragon 100 null 50
# Black Wyrm null 200 null
# Red Dragon 120 500 70
# Blue Drake null null null
# Blue Drake 80 300 null
dragon_stats()
