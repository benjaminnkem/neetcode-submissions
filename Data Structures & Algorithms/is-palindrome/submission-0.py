class Solution:
    def isPalindrome(self, s: str) -> bool:
        reversed_clean: str = ""
        for char in s.lower():
            reversed_clean += char if char.isalpha() or char.isnumeric() else ""

        return reversed_clean[::-1] == reversed_clean
