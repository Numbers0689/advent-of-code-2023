inputFile = open('input.txt')
eachLine = []
for line in inputFile:
    eachLine.append(line)


def makeWordList(word):
    wordList = []
    for letter in word:
        wordList.append(letter)

    return wordList

def makeNumList(wordList):
    numList = []
    for alph in wordList:
        if alph.isnumeric():
            numList.append(alph)

    return numList

def makeNum(numList):
    num = ''
    if len(numList) >= 2:
        num = numList[0] + numList[-1]
    else:
        num = numList[0] * 2

    return int(num)


total = 0
for word in eachLine:
    wordList = makeWordList(word)
    numList = makeNumList(wordList)
    num = makeNum(numList)
    total += num
    
print(total)