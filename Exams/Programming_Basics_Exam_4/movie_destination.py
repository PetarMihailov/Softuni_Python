budget = float(input())  
destination = input() 
season = input()  
days = int(input())  

prices = {
    "Dubai": {"Winter": 45000, "Summer": 40000},
    "Sofia": {"Winter": 17000, "Summer": 12500},
    "London": {"Winter": 24000, "Summer": 20250},
}

price_per_day = prices[destination][season]
total_cost = price_per_day * days

if destination == "Dubai":
    total_cost *= 0.7  
elif destination == "Sofia":
    total_cost *= 1.25  

difference = abs(budget - total_cost)

if budget >= total_cost:
    print(f"The budget for the movie is enough! We have {difference:.2f} leva left!")
else:
    print(f"The director needs {difference:.2f} leva more!")
