control_minutes = int(input())
control_seconds = int(input())
track_length = float(input())
time_per_100m = int(input())

control_time = control_minutes * 60 + control_seconds

total_time = (track_length / 100) * time_per_100m
delay_count = track_length / 120
total_time -= delay_count * 2.5

if total_time <= control_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    difference = total_time - control_time
    print("No, Marin failed! He was {:.3f} second slower.".format(difference))
