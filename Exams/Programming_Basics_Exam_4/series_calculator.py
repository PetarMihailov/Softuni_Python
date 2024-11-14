import math

series_name = input()  
seasons = int(input())  
episodes_per_season = int(input())  
episode_duration = float(input())  

advertisements_time = 0.20 * episode_duration  
total_episode_time = episode_duration + advertisements_time  

total_time = 0

for season in range(seasons):
    season_time = episodes_per_season * total_episode_time + 10  
    total_time += season_time

total_time_minutes = math.floor(total_time)

print(f"Total time needed to watch the {series_name} series is {total_time_minutes} minutes.")
