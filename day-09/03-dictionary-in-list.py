travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["paris","dijon"]
    },
    {
        "country": "Germany",
        "visits": 4,
        "cities": ["berlin","stuttgart"]
    }
]

def add_new_country(country, number_of_vists, cities):
    return travel_log.append({
        "country": country,
        "visits":number_of_vists,
        "cities":cities
     })

add_new_country("Russia",2, ["Moscow","St. Petersburg"])
print(travel_log) 
