# duplicates
def dupes(numbers):
    i = 0
    while 1 < len(numbers)-1:
        j = i+1
        while j < len(numbers):
            if numbers[i] == numbers[j]:
                return True
            j+=1
        i+=1
    return False

print(dupes([3,5,2,7,5]))

text = "here are some quotation marks inside of a string: \"\'\'\""
print(text)

rocky = ["Rocky","Shane","Texas Heeler"]
maple = ["Maple", "Amanda", "Hound"]
bofur = ["Bofur", "Ronda", "Corgi"]
dogs = [rocky,maple,bofur]

with open('dogs.csv', "w") as outfile:
    outfile.write(",".join(["Dog","Owner","Breed"]))
    for dog in dogs:
        outfile.write("\n"+",".join(dog))