# find area
def findArea(length, width):
    area = length * width
    print("area is : ", area)


# find perimeter
def findPerimeter(length, width):
    perimeter = (2 * (length + width))
    print("perimeter is : ", perimeter)


# find max number
def findMax(a, b):
    if a > b:
        print("Max number is ", a)
    else:
        print("Max number is ", b)


# find palindrome
def findPalindrome(checkword):
    tmpWord = checkword[::-1]
    if tmpWord == checkword:
        print("word", checkword, "is palindrome")
    else:
        print("word", checkword, "is not palindrome")


# distinct elements from the given list
def unique_list(l):
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    print(x)


# create multiplication table
def multiplicationTable(num):
    for i in range(1, 11):
        print(num, "x", i, "=", num * i)


# find no of uppercase and lowercase letters
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
    print("no of uppercase letters : ", noUpper)
    print("no of lowercase letters : ", noLower)


# calling the user defined functions

findArea(3, 4)
findPerimeter(3, 4)

num1 = 10
num2 = 20
findMax(num1, num2)

word = "MOM"
findPalindrome(word)

list1 = [1, 1, 2, 3, 3, 4, 5, 6, 5, 4, 4, 6, 6, 7, 5, 8, 9]
unique_list(list1)

multiplicationTable(2)

findLowerUpper("appLab")