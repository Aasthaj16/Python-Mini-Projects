import random
logo = ('''
|    |  ____         ____          ____
|____| |    | |\  | |      |\  /| |    | |\  |
|    | |____| | \ | |  ___ | \/ | |____| | \ |
|    | |    | |  \| |____| |    | |    | |  \|
''')

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''',
          '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', ]

print(logo)

wordList = ["aastha", "hello", "twist", "python", "water",
            "fire", "breathe", "lost", "wonder", "true", "false", "rain", "train", "movie", "hiteshi", "sorry", "oxford", "hangman",
            "number", "aastha", "palak", "ishika", "rocket", "left", "enter", "choice", "laptop", "computer", "internet", "instagram",
            "mobile", "kitchen", "travel", "paris", "london", "oven", "pizza", "catch", "match", "patch", "yashika"]


word = random.choice(wordList)
# print("Word:", word)
stageLength = len(stages)
val = 0
answer = []
wordList = []
print("Length of word", len(word))
for j in range(len(word)):
    answer.append("_")
print(" ".join(answer))
while val < stageLength:
    playerChoice = input("Enter your choice: ")
    if playerChoice in wordList:
        print("You've already entered", playerChoice.upper())
        continue
    if playerChoice in word:
        listOfIndexes = [i for i, x in enumerate(
            word) if x == playerChoice]
        for ltr in listOfIndexes:
            answer[ltr] = playerChoice
        print(" ".join(answer))
    else:
        print(stages[val])
        val += 1
    wordList.append(playerChoice)
    # print(wordList)
    if "_" not in answer:
        break
    if val == stageLength - 1:
        print("-------Last chance left--------")

if val != stageLength and "_" not in answer:
    print("--------------CONGRATS, YOU WON!---------------")
else:
    print("---------SORRY, YOU LOST!----------")
print("The word was:", word.upper(), ".")
