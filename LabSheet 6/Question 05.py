def findLowerUpper(newWord):
    noUpper = 0
    noLower = 0
    for letter in newWord:
        if letter.isupper():
            noUpper += 1
        elif letter.islower():
            noLower += 1
        else:
            pass
    print("Number of uppercase letters : ", noUpper)
    print("Number of lowercase letters : ", noLower)


findLowerUpper("Application Laboratory")

