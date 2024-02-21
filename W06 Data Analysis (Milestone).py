totalMaxCountry = ["","","","-1"]
totalMinCountry = ["","","","9999"]

with open("life-expectancy.csv") as file:

    next(file)

    for line in file:
        line = line.strip()
        lineInfoList = line.split(",")
        #print (lineInfoList)

        if float(totalMaxCountry[3]) < float(lineInfoList[3]):
            totalMaxCountry = lineInfoList
        
        if float(totalMinCountry[3]) > float(lineInfoList[3]):
            totalMinCountry = lineInfoList

print(f"The overall max life expectancy is: {totalMaxCountry[3]} from {totalMaxCountry[0]} in {totalMaxCountry[2]}")
print(f"The overall min life expectancy is: {totalMinCountry[3]} from {totalMinCountry[0]} in {totalMinCountry[2]}")