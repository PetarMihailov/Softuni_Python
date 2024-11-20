frames_count = int(input())
frame_type = input()
delivery_method = input()

if frames_count < 10:
    print("Invalid order")
    exit()

price_per_frame = 0
discount = 0

if frame_type == "90X130":
    price_per_frame = 110
    if frames_count > 60:
        discount = 0.08
    elif frames_count > 30:
        discount = 0.05
elif frame_type == "100X150":
    price_per_frame = 140
    if frames_count > 80:
        discount = 0.10
    elif frames_count > 40:
        discount = 0.06
elif frame_type == "130X180":
    price_per_frame = 190
    if frames_count > 50:
        discount = 0.12
    elif frames_count > 20:
        discount = 0.07
elif frame_type == "200X300":
    price_per_frame = 250
    if frames_count > 50:
        discount = 0.14
    elif frames_count > 25:
        discount = 0.09

total_price = frames_count * price_per_frame
total_price -= total_price * discount

if delivery_method == "With delivery":
    total_price += 60

if frames_count > 99:
    total_price -= total_price * 0.04

print(f"{total_price:.2f} BGN")
