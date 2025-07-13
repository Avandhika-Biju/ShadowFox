countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}
city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

country1 = None
country2 = None
for country, cities in countries.items():
    if city1 in cities:
        country1 = country
    if city2 in cities:
        country2 = country
if country1 and country2:
    if country1 == country2:
        print(f"Both cities are in {country1}")
    else:
        print("They don't belong to the same country")
else:
    print("One or both cities are not in the list.")



# output 1

# Enter the first city: Mumbai
# Enter the second city: Chennai   
# Both cities are in India

# output 2

# Enter the first city: Sydney
# Enter the second city: Dubai
# They don't belong to the same country