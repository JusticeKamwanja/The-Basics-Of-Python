# Write a function called city_country() that takes in the name of a city and its country.
# The function should return a string formatted like this: "Santiago, Chile"
# Call your function with at least three city-country pairs, and print the value that’s returned.

def city_country(city, country):
    string = (f'"{city}, {country}"')
    return string

print(city_country('Kampala', 'Uganda'))
print(city_country('Nairobi', 'Kenya'))
print(city_country('Dar-es-Salaam', 'Tanzania'))

