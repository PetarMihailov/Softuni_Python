import math

shooting_time = int(input())  
scenes_count = int(input())  
scene_duration = int(input()) 

prep_time = shooting_time * 0.15  
scenes_time = scenes_count * scene_duration  
total_time_needed = prep_time + scenes_time

if total_time_needed <= shooting_time:
    remaining_time = math.ceil(shooting_time - total_time_needed)
    print(f"You managed to finish the movie on time! You have {remaining_time} minutes left!")
else:
    extra_time = math.ceil(total_time_needed - shooting_time)
    print(f"Time is up! To complete the movie you need {extra_time} minutes.")
