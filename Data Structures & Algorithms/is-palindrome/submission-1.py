class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''.join(char for char in s if char.isalnum()).lower()
        n = len(newStr)

        return newStr == newStr[::-1]