capacity = int(input())  
total_income = 0  
occupied_seats = 0  

while True:
    command = input()  

    if command == "Movie time!":
        print(f"There are {capacity - occupied_seats} seats left in the cinema.")
        break

    people = int(command)  

    if occupied_seats + people > capacity:
        print("The cinema is full.")
        break

    occupied_seats += people

    current_income = people * 5
    if people % 3 == 0:
        current_income -= 5  

    total_income += current_income  

print(f"Cinema income - {total_income} lv.")
