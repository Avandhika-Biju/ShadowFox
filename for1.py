import random
num_rolls = 20
count_6 = 0
count_1 = 0
count_two_6s_in_a_row = 0
prev_roll = None
print("Rolling the die...\n")
for i in range(num_rolls):
    roll = random.randint(1, 6)
    print(f"Roll {i+1}: {roll}")
    if roll == 6:
        count_6 += 1
        if prev_roll == 6:
            count_two_6s_in_a_row += 1
    if roll == 1:
        count_1 += 1
    prev_roll = roll
print("\n--- Statistics ---")
print("Total rolls:", num_rolls)
print("Number of 6s rolled:", count_6)
print("Number of 1s rolled:", count_1)
print("Number of times two 6s in a row:", count_two_6s_in_a_row)



# output

# Rolling the die...

# Roll 1: 4
# Roll 2: 1
# Roll 3: 6
# Roll 4: 4
# Roll 5: 3
# Roll 6: 5
# Roll 7: 3
# Roll 8: 6
# Roll 9: 6
# Roll 10: 6
# Roll 11: 5
# Roll 12: 2
# Roll 13: 6
# Roll 14: 3
# Roll 15: 1
# Roll 16: 5
# Roll 17: 2
# Roll 18: 3
# Roll 19: 1
# Roll 20: 6

# --- Statistics ---
# Total rolls: 20
# Number of 6s rolled: 6
# Number of 1s rolled: 3
# Number of times two 6s in a row: 2
