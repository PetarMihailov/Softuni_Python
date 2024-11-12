won_matches = 0
lost_matches = 0
total_matches = 0

# Четем турнирите докато не получим командата "End of tournaments"
while True:
    tournament_name = input()  # Четем името на турнира
    
    if tournament_name == "End of tournaments":
        break  # Ако е "End of tournaments", спираме да четем турнири
    
    # Четем броя на мачовете за текущия турнир
    num_matches = int(input())
    
    # Обработваме всеки мач за текущия турнир
    for match_number in range(1, num_matches + 1):
        # Четем точките на Деси и на противниковия отбор
        desi_points = int(input())
        opponent_points = int(input())
        
        # Увеличаваме общия брой мачове
        total_matches += 1
        
        # Проверяваме дали Деси е спечелила или загубила
        if desi_points > opponent_points:
            won_matches += 1
            print(f"Game {match_number} of tournament {tournament_name}: win with {desi_points - opponent_points} points.")
        else:
            lost_matches += 1
            print(f"Game {match_number} of tournament {tournament_name}: lost with {opponent_points - desi_points} points.")
    
# Изчисляваме процента спечелени и загубени мачове
win_percentage = (won_matches / total_matches) * 100
lost_percentage = (lost_matches / total_matches) * 100

# Отпечатваме процентите
print(f"{win_percentage:.2f}% matches win")
print(f"{lost_percentage:.2f}% matches lost")
