countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}
city = input("Enter a city name: ")
found = False
for country, cities in countries.items():
    if city in cities:
        print(f"{city} is in {country}")
        found = True
        break
if not found:
    print(f"{city} is not in the list.")


# output 

# Enter a city name: Abu Dhabi
# Abu Dhabi is in UAE
