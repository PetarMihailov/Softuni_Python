import math

record_in_seconds = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

base_time = distance_in_meters * time_per_meter
slowdown_time = math.floor(distance_in_meters / 50) * 30
total_time = base_time + slowdown_time

if total_time < record_in_seconds:
    print(f"Yes! The new record is {total_time:.2f} seconds.")
else:
    difference = total_time - record_in_seconds
    print(f"No! He was {difference:.2f} seconds slower.")
