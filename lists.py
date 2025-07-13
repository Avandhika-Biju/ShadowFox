justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print("1. Initial Justice League:", justice_league)

print("2. Number of members:", len(justice_league))

justice_league.append("Batgirl")
justice_league.append("Nightwing")
print("3. After adding Batgirl and Nightwing:", justice_league)

justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print("4. After making Wonder Woman the leader:", justice_league)

aquaman_index = justice_league.index("Aquaman")
flash_index = justice_league.index("Flash")

if aquaman_index > flash_index:
    aquaman_index, flash_index = flash_index, aquaman_index

justice_league.remove("Superman")

justice_league.insert(flash_index, "Superman")
print("5. After placing Superman between Aquaman and Flash:", justice_league)

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("6. After crisis, new Justice League:", justice_league)

justice_league.sort()
print("7. Sorted Justice League:", justice_league)

print("8. New Leader (0th index):", justice_league[0])    



# output

# 1. Initial Justice League: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern']
# 2. Number of members: 6
# 3. After adding Batgirl and Nightwing: ['Superman', 'Batman', 'Wonder Woman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
# 4. After making Wonder Woman the leader: ['Wonder Woman', 'Superman', 'Batman', 'Flash', 'Aquaman', 'Green Lantern', 'Batgirl', 'Nightwing']
# 5. After placing Superman between Aquaman and Flash: ['Wonder Woman', 'Batman', 'Flash', 'Aquaman', 'Superman', 'Green Lantern', 'Batgirl', 'Nightwing']
# 6. After crisis, new Justice League: ['Cyborg', 'Shazam', 'Hawkgirl', 'Martian Manhunter', 'Green Arrow']
# 7. Sorted Justice League: ['Cyborg', 'Green Arrow', 'Hawkgirl', 'Martian Manhunter', 'Shazam']     
# 8. New Leader (0th index): Cyborg
