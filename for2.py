total_jumping_jacks = 100
completed = 0
set_size = 10

while completed < total_jumping_jacks:
    completed += set_size
    print(f"You have completed {completed} jumping jacks.")

    if completed == total_jumping_jacks:
        print("🎉 Congratulations! You completed the workout.")
        break

    tired = input("Are you tired? (yes/no): ").lower()

    if tired in ["yes", "y"]:
        skip = input("Do you want to skip the remaining sets? (yes/no): ").lower()
        if skip in ["yes", "y"]:
            print(f"You completed a total of {completed} jumping jacks.")
            break
        elif skip in ["no", "n"]:
            remaining = total_jumping_jacks - completed
            print(f"Okay, keep going! {remaining} jumping jacks remaining.\n")
    elif tired in ["no", "n"]:
        remaining = total_jumping_jacks - completed
        print(f"Keep going! {remaining} jumping jacks remaining.\n")
    else:
        print("Invalid input. Assuming you're not tired. Let's continue!\n")



# output 1

# You have completed 10 jumping jacks.
# Are you tired? (yes/no): no
# Keep going! 90 jumping jacks remaining.

# You have completed 20 jumping jacks.
# Are you tired? (yes/no): no
# Keep going! 80 jumping jacks remaining.

# You have completed 30 jumping jacks.
# Are you tired? (yes/no): yes
# Do you want to skip the remaining sets? (yes/no): yes
# You completed a total of 30 jumping jacks.