capacity = float(input())

current_space = capacity
loaded_baggage_count = 0

while True:
    suitcase_volume = input()

    if suitcase_volume == "End":
        print("Congratulations! All suitcases are loaded!")
        break
        
    suitcase_volume = float(suitcase_volume)
    
    if (loaded_baggage_count + 1) % 3 == 0:
        suitcase_volume *= 1.1

    if current_space >= suitcase_volume:
        current_space -= suitcase_volume
        loaded_baggage_count += 1
    else:
        print("No more space!")
        break

print(f"Statistic: {loaded_baggage_count} suitcases loaded.")
