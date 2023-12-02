def main():

    input = open("G:\\python\\AoC2023\\Inputs\\test.txt", "r")


#make a list of the lines

    lines = input.read().split('\n')

    #function to turn each line into only the digits which appear in it
    def distill(string):
        numStringList = [-1] * len(string)
        if string.find("one") != -1:
            numStringList[string.find("one")] = 1
        if string.find("two") != -1:
            numStringList[string.find("two")] = 2
        if string.find("three") != -1:
            numStringList[string.find("three")] = 3
        if string.find("four") != -1:
            numStringList[string.find("four")] = 4
        if string.find("five") != -1:
            numStringList[string.find("five")] = 5
        if string.find("six") != -1:
            numStringList[string.find("six")] = 6
        if string.find("seven") != -1:
            numStringList[string.find("seven")] = 7
        if string.find("eight") != -1:
            numStringList[string.find("eight")] = 8
        if string.find("nine") != -1:
            numStringList[string.find("nine")] = 9

        return numStringList


    firstNum = 0
    lastNum = 0

    doubleString = "-1"

    total = 0

    for i in lines:
        firstNum = 0
        lastNum = 0

        #print(i)

        iNumeric = distill(i)

        for j in iNumeric:
            if firstNum == 0:
                firstNum = j
        for z in reversed(iNumeric):
            if lastNum == 0:
                lastNum = z

        doubleString = str(firstNum) + str(lastNum)
        total += int(doubleString)

    print(total)

main()

