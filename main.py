def palindrom(word):
    """
    Function checks if the argument is a palindrome
    Argument: word
    """
    if type(word)!=str:
        r=False
        return(r)
    else:
        x=len(word)
        while x!=0:
            if word[x-1]!=word[-x]:
                r=False
                return(r)
            else:
                x=x-1
        if x==0:
            r=True
            return(r)
palindrom("ab")