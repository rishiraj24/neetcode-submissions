class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ''.join(char for char in s if char.isalnum()).lower()
        n = len(newStr)

        for i in range(len(newStr)):
            if newStr[i] == newStr[n-i-1]:
                continue
            else:
                return False
        return True