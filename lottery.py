import random

RANDOM_TIME = 100000

player_lst = ["Ye", "Kevin", "Chao"]
player_amount = len(player_lst)
lottery = {}

for name in player_lst:
    lottery[name] = 0

for shift in range(player_amount):
    random_lst = [0] * player_amount
    for _ in range(RANDOM_TIME):
        random_lst[random.randint(0, player_amount - 1)] += 1

    # Shift the order of the player_lst list, make it more fair
    for idx in range(len(random_lst)):
        lottery[player_lst[(shift + idx) % player_amount]] += random_lst[idx] 

for name in player_lst:
    print("Player_lst - {}, count: {}".format(name, lottery[name]))

print("Winner: {}".format(max(lottery, key=lottery.get)))

