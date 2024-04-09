import random 

listOfWords = ["british", "suave", "integrity", "accent", "evil", "genius", "Downton"]

myWord = random.choice(listOfWords)
print(myWord)
print("Hangman")
counter = 0
while True:
  letter = input("Choose a letter: ")
  if letter in myWord:
    print("Correct!")
    counter += 1
    if counter == len(myWord):
      print("You won with", counter, "lives left.")
      break
  else:
    print("Nope, not in there.")
    counter += 1
    if counter == 6:
      print("You lost!")
      break
