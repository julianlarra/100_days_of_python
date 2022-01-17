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

# Write the function that will allow new countries

def add_new_country(country_visit, times_visited, cities_visited, ):
 travel_log.append([
   {
    "country":country_visit,
    "Visits":times_visited,
    "Cities":cities_visited
}
] )




add_new_country ( (input(f"Insert new country\n")),(input(f"How many times do I visit the country?\n") ), (input(f"what cities do you visit?\n")))
print(travel_log)
