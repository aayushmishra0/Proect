def countWordsFromFile():
    fileName = input('enter the filename: ')
    numberOfWords = 0
    file = open(fileName,'r')
    for line in file:
        words = line.split()
        numberOfWords = numberOfWords+len(words)
    print('words')
    print(numberOfWords)
countWordsFromFile()