def pond_water_volume(radius):
    pi = 3.14
    area = pi * (radius ** 2)
    water_per_sqm = 1.4
    total_water = area * water_per_sqm
    
    return int(total_water)

radius = 84
total_liters = pond_water_volume(radius)

print("Total amount of water in the pond:", total_liters, "liters")
  

# output

# The number 145 in o-format is: 221