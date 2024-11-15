best_movie = ""
max_score = float('-inf')
movie_count = 0

while movie_count < 7:
    movie_title = input()

    if movie_title == "STOP":
        break

    score = 0
    movie_length = len(movie_title)

    for char in movie_title:
        score += ord(char)  
        if char.islower():  
            score -= 2 * movie_length  
        elif char.isupper():  
            score -= movie_length  

    if score > max_score:
        best_movie = movie_title
        max_score = score

    movie_count += 1

if movie_count == 7:
    print("The limit is reached.")

print(f"The best movie for you is {best_movie} with {max_score} ASCII sum.")
