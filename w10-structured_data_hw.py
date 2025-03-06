import csv
from typing import Counter

with open('marriage_data_india.csv', mode='r', newline='', encoding="utf-8") as csvfile:
    shadishuda = csv.DictReader(csvfile)
    love_counter = Counter()
    for shadi in shadishuda:
        love_counter[shadi["Children_Count"]] += 1

    print(love_counter.most_common(3))
