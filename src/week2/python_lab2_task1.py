"""
Lab 3.1 – Simple Datasets and Aggregates

Goals:
- Create and manipulate Python lists and dictionaries.
- Compute aggregates such as sum, average, max, and min.

Instructions:
1. Create a list `temperatures` with daily temperatures for one week.
2. Create a dictionary `city_population` with at least 5 cities and their populations.
3. Compute:
   - The average temperature.
   - The maximum and minimum population.
   - The total population of all cities.
4. Print your results in a clear, formatted way.
"""

# TODO: Create the datasets - up to you to fill in the data
temperatures = [12, 15, 14, 10, 9, 11, 13]
city_population = {
    "Riga": 632614,
    "Vilnius": 588412,
    "Tallinn": 453996,
    "Kaunas": 298607,
    "Tartu": 91248,
}

# TODO: Compute aggregates
average_temperature = sum(temperatures) / len(temperatures)
largest_city = None
largest_population = -1
for city in city_population:
    if city_population[city] > largest_population:
        largest_population = city_population[city]
        largest_city = city
total_population = sum(city_population.values())

# TODO: Print results
print("Average temperature:", average_temperature)
print("Largest city:", largest_city, "-", largest_population)
print("Total population:", total_population)
