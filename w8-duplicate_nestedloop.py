x = [3,5,2,7,5]
i = 0
while i < len(x)-1:
    j = i + 1
    while j < len(x):
        if x[i] == x[j]:
            print("Duplicate")
        j += 1
    i += 1


# how to print each element of the list separately
x=[[0 ,1 ,2 ,3 ,4 ,5],
   [10,11,12,13,14,15],
   [20,21,22,23,24,25]]
for i in x:
    for j in i:
        
        print(j)

# return change
DENOMINATIONS = [100,20,10,5,1,0.25,0.1,0.5,0.01]

def change(cost, payment):
    change_types = []
    remaining_change = payment - cost

    for denomination in DENOMINATIONS:
        if cost > payment:
            return []
        if cost == payment:
            return []
        if remaining_change >= denomination:
            x = int(remaining_change/denomination)
            change_types.append([denomination, x])
            remaining_change = remaining_change - (denomination*x)
    return change_types

print(change(5,0))  

