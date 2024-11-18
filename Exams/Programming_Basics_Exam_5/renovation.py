import math

wall_height = int(input())  
wall_width = int(input())  
non_painted_percentage = int(input())  

total_area = wall_height * wall_width * 4
paintable_area = total_area * (1 - non_painted_percentage / 100)
paintable_area = math.ceil(paintable_area)  

while True:
    command = input()  
    if command == "Tired!":
        print(f"{paintable_area} quadratic m left.")
        break

    liters_paint = int(command)  
    paintable_area -= liters_paint  

    if paintable_area <= 0:
        if paintable_area < 0:
            print(f"All walls are painted and you have {abs(paintable_area)} l paint left!")
        else:
            print("All walls are painted! Great job, Pesho!")
        break
