from typing import List

# https://neetcode.io/problems/is-palindrome
def isPalindrome(s: str) -> bool:
    from_bottom = 0
    from_top = len(s)-1
    get_out = lambda: from_top <= from_bottom or from_bottom >= len(s) or from_top < 0
    while not get_out():
        while not get_out() and not s[from_bottom].isalnum():
            from_bottom = from_bottom+1
        while not get_out() and not s[from_top].isalnum():
            from_top = from_top-1
        if s[from_bottom].lower() != s[from_top].lower(): return False
        from_bottom = from_bottom +1
        from_top = from_top - 1
    return True