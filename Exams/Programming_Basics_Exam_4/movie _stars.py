budget = float(input())

while True:
    actor_name = input()  
    if actor_name == "ACTION":  
        print(f"We are left with {budget:.2f} leva.")
        break

    if len(actor_name) > 15: 
        salary = 0.20 * budget 
    else:
        salary = float(input()) 

    if salary > budget:  
        print(f"We need {salary - budget:.2f} leva for our actors.")
        break

    budget -= salary 
