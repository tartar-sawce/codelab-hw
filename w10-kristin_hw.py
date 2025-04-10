import csv
with open('Birding_Trail_Locations.csv', newline='') as csvfile:
    trailreader = csv.DictReader(csvfile)
    Bird_Conservation_Area = []
    Not_Bird_Conservation_Area = []
    for trail in trailreader:
        if(trail["Bird Conservation Area"] == "true"):
            Bird_Conservation_Area.append(trail["NYS Birding Trail Site Name"])
        else:
            Not_Bird_Conservation_Area.append(trail["NYS Birding Trail Site Name"])
#Sort lists alphabetically
Bird_Conservation_Area.sort()
Not_Bird_Conservation_Area.sort()
 
#Find the number of sites in list, then print the list with one item per line
Bird_Conservation_Number = len(Bird_Conservation_Area)
print("The following", Bird_Conservation_Number, "trails are designated as Bird Conservation Areas:")
print(*Bird_Conservation_Area,sep='\n')
#Find the number of sites in list, then print the list with one item per line
Not_Bird_Conservation_Number = len(Not_Bird_Conservation_Area)
print('\n'"The following", Not_Bird_Conservation_Number, "trails are not designated as Bird Conservation Areas:")
print(*Not_Bird_Conservation_Area,sep='\n')