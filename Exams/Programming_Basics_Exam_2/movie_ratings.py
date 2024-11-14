num_films = int(input())

highest_rating = -1
lowest_rating = 11
highest_rating_film = ""
lowest_rating_film = ""
total_rating = 0


for _ in range(num_films):
    film_name = input()
    rating = float(input())

    total_rating += rating

    if rating > highest_rating:
        highest_rating = rating
        highest_rating_film = film_name

    if rating < lowest_rating:
        lowest_rating = rating
        lowest_rating_film = film_name

average_rating = total_rating / num_films

print(f"{highest_rating_film} is with highest rating: {highest_rating:.1f}")
print(f"{lowest_rating_film} is with lowest rating: {lowest_rating:.1f}")
print(f"Average rating: {average_rating:.1f}")
