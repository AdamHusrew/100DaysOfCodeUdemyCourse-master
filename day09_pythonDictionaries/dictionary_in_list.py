travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


def add_new(country_name, num_of_visits, list_of_cities):
    adding = {
        "country": country_name,
        "visits": num_of_visits,
        "cities": list_of_cities
    }

    travel_log.append(adding)


# to be added to the travel_log. 👇

add_new("Russia", 4, ["Moscow", "St. Petersburg"])

print("----------------------------")
print(travel_log)
