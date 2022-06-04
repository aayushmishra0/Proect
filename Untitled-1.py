a = input("Enter a String: ")
characterCount = 0
wordCount = 1
for i in a:
    characterCount = characterCount +1
    if (i == ' '):
        wordCount = wordCount+1

print(characterCount)
print(wordCount)