movie_name = input()
days = int(input())
tickets_per_day = int(input())
ticket_price = float(input())
cinema_percentage = int(input())

total_income = days * tickets_per_day * ticket_price
profit_for_studio = total_income * (1 - cinema_percentage / 100)

print(f"The profit from the movie {movie_name} is {profit_for_studio:.2f} lv.")
