with open("500DayFruitData.txt", "r") as file:
    data = [line.strip().split() for line in file.readlines()[1:]]

fruit_data = {
    "apple": [],
    "banana": [],
    "strawberry": []
}

for line in data:
    day, fruit, amount = line
    fruit_data[fruit].append(int(amount))

from Ryder_Kos_Stats import Mean, Median

fruit_stats = {}

for fruit, amounts in fruit_data.items():
    if len(amounts) > 0:
        mean_fruit = Mean(amounts)
        median_fruit = Median(amounts)
        fruit_stats[fruit] = (mean_fruit, median_fruit)

for fruit, (mean_value, median_value) in fruit_stats.items():
    print(f"Mean number of {fruit}s eaten: {round(mean_value, 2)}")
    print(f"Median number of {fruit}s eaten: {median_value}")
    print()

all_fruits = [amount for amounts in fruit_data.values() for amount in amounts]
if len(all_fruits) > 0:
    overall_mean = Mean(all_fruits)
    overall_median = Median(all_fruits)
    print(f"Mean number of all fruits eaten: {round(overall_mean, 2)}")
    print(f"Median number of all fruits eaten: {overall_median}")
