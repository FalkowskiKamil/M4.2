def palindrom(word):
    """
    Function checks if the argument is a palindrome
    Argument: word
    """
    if type(word)!=str:
        return False
    else:
        if word==word[::-1]:
            return True
        else:
            return False
palindrom("kajak")
