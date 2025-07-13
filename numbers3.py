def calculate_speed(distance_m, time_min):
    time_sec = time_min * 60
    speed = distance_m / time_sec
    return int(speed)

distance = 490
time_minutes = 7

speed_mps = calculate_speed(distance, time_minutes)
print("Speed:", speed_mps, "m/s")



# output 

# Speed: 1 m/s