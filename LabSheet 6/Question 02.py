def findPalindrome(checkword):
    tmpWord = checkword[::-1]
    if tmpWord == checkword:
        print("word", checkword, "is palindrome")
    else:
        print("word", checkword, "is not palindrome")


findPalindrome("mom")
findPalindrome("applab")
