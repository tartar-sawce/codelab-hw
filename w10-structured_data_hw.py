import csv
from typing import Counter

with open('marriage_data_india.csv', mode='r', newline='', encoding="utf-8") as csvfile:
    shadishuda = csv.DictReader(csvfile)
    love_counter = Counter()
    for shadi in shadishuda:
        love_counter[shadi["Children_Count"]] += 1

    print(love_counter.most_common(3))

# Good idea to print and then exit, to check if your code is working.

import csv
from typing import Counter

with open('marriage_data_india.csv', mode='r', newline='', encoding="utf-8") as csvfile:
    shadishuda = csv.DictReader(csvfile)
    
    love_total = 0
    love_parental_approval = 0
    love_diff_caste = 0
    for shadi in shadishuda:
        if shadi["Marriage_Type"] == "Love":
            love_total += 1
            if shadi["Parental_Approval"] == "Yes":
                love_parental_approval += 1
                if shadi["Inter-Caste"] == "Yes":
                    love_diff_caste += 1
    
    print(love_parental_approval)
    print(love_total)
    print(love_parental_approval/love_total)
    print(str(love_diff_caste/love_total) + "% of intercaste love marriages were fully approved by parents.")


#how to create a json and open it to use:
# with open("marriage.json", "w", encoding="utf-8") as json_file: 
#     json.dump(marriages, json_file, indent=4)

# with open("marriage.json","r",encoding="utf-8") as in_file:
#     marriages2 = json.load(in_file)
# print(marriages[532])
# print(marriages2[532])