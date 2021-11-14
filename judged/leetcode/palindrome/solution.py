import string

def isPalindrome(s: str) -> bool:

    s = [ i for i in s.lower() if i in string.ascii_lowercase + string.digits ]

    if len(s) < 2:
        return True

    left = 0
    right = len(s)-1

    while left <= len(s) // 2:
        if s[left] != s[right]:
            return False

        left += 1
        right -= 1

    return True