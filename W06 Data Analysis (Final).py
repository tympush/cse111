#Creativity:
#Added an option to give a country of interest similar to the specific year of interest
#Added the highest drop and increase between one year to the next in a country, in the overall data section
#Minor structure improvements (white space and rounding) to make it easier to read, as well as adding the overall average for the overall section

averageOverallList = []
totalMaxCountry = ["","","","-1"]
totalMinCountry = ["","","","9999"]

averageInterestYearList = []
totalMaxInterestYear = ["","","","-1"]
totalMinInterestYear = ["","","","9999"]

averageInterestCountryList = []
totalMaxInterestCountry = ["","","","-1"]
totalMinInterestCountry = ["","","","9999"]

previousList = []
highestDrop = 0
highestIncrease = 0

previousDropList = []
previousIncreaseList = []
highestDropList = []
highestIncreaseList = []

interestYear = input("Enter the year of interest: ")
interestCountry = input("Enter the country of interest: ")

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

        if len(previousList) != 0 and previousList[0] == lineInfoList[0] and (int(previousList[2]) + 1.0) == int(lineInfoList[2]):
            
            drop = float(previousList[3]) - float(lineInfoList[3])
            if drop > highestDrop:
                highestDropList = lineInfoList
                previousDropList = previousList
                highestDrop = drop
            
            increase = float(lineInfoList[3]) - float(previousList[3])
            if increase > highestIncrease:
                highestIncreaseList = lineInfoList
                previousIncreaseList = previousList
                highestIncrease = increase
        
        previousList = lineInfoList



        if lineInfoList[2] == interestYear:

            if float(totalMaxInterestYear[3]) < float(lineInfoList[3]):
                totalMaxInterestYear = lineInfoList
            
            if float(totalMinInterestYear[3]) > float(lineInfoList[3]):
                totalMinInterestYear = lineInfoList
            
            averageInterestYearList.append(float(lineInfoList[3]))
        



        if lineInfoList[0].lower() == interestCountry.lower():

            if float(totalMaxInterestCountry[3]) < float(lineInfoList[3]):
                totalMaxInterestCountry = lineInfoList
            
            if float(totalMinInterestCountry[3]) > float(lineInfoList[3]):
                totalMinInterestCountry = lineInfoList
            
            averageInterestCountryList.append(float(lineInfoList[3]))
        


        averageOverallList.append(float(lineInfoList[3]))


print("\nFor the dataset overall:")

average = sum(averageOverallList) / len(averageOverallList)
print(f"The overall average life expectancy across all countries is {float(average):.2f}")

print(f"The overall max life expectancy is: {float(totalMaxCountry[3]):.2f} from {totalMaxCountry[0]} in {totalMaxCountry[2]}")
print(f"The overall min life expectancy is: {float(totalMinCountry[3]):.2f} from {totalMinCountry[0]} in {totalMinCountry[2]}")

print(f"The highest drop is {float(highestDrop):.2f} in {highestDropList[0]}, going from {float(previousDropList[3]):.2f} in {previousDropList[2]} to {float(highestDropList[3]):.2f} in {highestDropList[2]}")
print(f"The highest increase is {float(highestIncrease):.2f} in {highestIncreaseList[0]}, going from {float(previousIncreaseList[3]):.2f} in {previousIncreaseList[2]} to {float(highestIncreaseList[3]):.2f} in {highestIncreaseList[2]}")



print(f"\nFor the year {interestYear}:")

if len(averageInterestYearList) == 0:
    print("There is no data for this year.")
else:
    average = sum(averageInterestYearList) / len(averageInterestYearList)
    print(f"The average life expectancy across all countries was {float(average):.2f}")

    print(f"The max life expectancy was in {totalMaxInterestYear[0]} with {float(totalMaxInterestYear[3]):.2f}")
    print(f"The min life expectancy was in {totalMinInterestYear[0]} with {float(totalMinInterestYear[3]):.2f}")



print(f"\nFor the country {interestCountry.capitalize()}:")

if len(averageInterestCountryList) == 0:
    print("There is no data for this country.")
else:
    average = sum(averageInterestCountryList) / len(averageInterestCountryList)
    print(f"The average life expectancy across all years was {float(average):.2f}")

    print(f"The max life expectancy was in {totalMaxInterestCountry[2]} with {float(totalMaxInterestCountry[3]):.2f}")
    print(f"The min life expectancy was in {totalMinInterestCountry[2]} with {float(totalMinInterestCountry[3]):.2f}")