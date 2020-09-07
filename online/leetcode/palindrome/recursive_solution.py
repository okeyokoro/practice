def isPalindrome(st: str):
    if len(st) < 2:
        return True

    def recurse(s):
        if len(s) <= 1:
            return True
        if s[0] != s[-1]:
            return False
        return recurse(s[1:-1])

    return recurse(st)

print(isPalindrome("abcdcba"))
