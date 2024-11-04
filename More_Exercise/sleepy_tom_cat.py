rest_days = int(input())

work_days = 365 - rest_days

play_time = work_days * 63 + rest_days * 127
diff = abs(play_time - 30000)
play_time_hours = diff // 60
play_time_minutes = diff % 60

if play_time > 30000:
    print(f"Tom will run away\n{play_time_hours} hours and {play_time_minutes} minutes more for play")
else:
    print(f"Tom sleeps well\n{play_time_hours} hours and {play_time_minutes} minutes less for play")
