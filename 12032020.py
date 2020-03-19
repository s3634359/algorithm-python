def create_palindrome(s):
    output = ""
    i = 0
    while (i < len(s)):
        if (s[i] == s[-1-i]):
            output = output + s[i]
        i += 1
    return output
    # return(s==s[-1::-1])

print(create_palindrome("abcdcbea"))
# True
print(create_palindrome("abccba"))
# False
print(create_palindrome("abccaa"))
# False
