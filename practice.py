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
