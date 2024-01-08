budget = float(input())
nums_video_cards = int(input())
nums_processors = int(input())
nums_ram_memory = int(input())

sum_video_cards = nums_video_cards * 250
sum_processors = nums_processors * (sum_video_cards * 0.35)
sum_ram_memory = nums_ram_memory * (sum_video_cards * 0.10)
total_sum = sum_video_cards + sum_processors + sum_ram_memory

if nums_video_cards > nums_processors:
    total_sum = total_sum - (total_sum * 0.15)
else:
    total_sum = total_sum

diff = abs(budget - total_sum)
if budget >= total_sum:
    print(f"You have {diff:.2f} leva left!")
else:
    print(f"Not enough money! You need {diff:.2f} leva more!")

