def city_country(city, country, population=''):
    description = f'{city.title()}, {country.title()} -population {population}' if population else f'{city.title()}, {country.title()}'
    return description
