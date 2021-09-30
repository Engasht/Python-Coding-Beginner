# Spyder Editor
# Created on Thu Sep 30 09:07:03 2021
# @author: Mani Mehrabi
# Part of a Python Bootcamp - Beginner
# 009 - 02 - Nesting Dictionary in List

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
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country, numberOfVisit, citiesVisited):
    new_log = {}
    new_log["country"] = country
    new_log["visits"] = numberOfVisit
    new_log["cities"] = citiesVisited
    travel_log.append(new_log)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)



