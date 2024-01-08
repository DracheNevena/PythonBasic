import math

record_sec = float(input())
distance_m = float(input())
time_for_one_meter = float(input())


time_for_swimming = distance_m * time_for_one_meter
water_resistance = math.floor(distance_m / 15) * 12.5
total_time = time_for_swimming + water_resistance


if record_sec <= total_time:
    diff = total_time - record_sec
    print(f"No, he failed! He was {diff:.2f} seconds slower.")

else:
    print(f"Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
