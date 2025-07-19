class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join(char for char in s if char.isalpha())
        s = s.replace(' ', '')
        s = s.casefold()

        print(s)
        print(s[::-1])
        return s == s[::-1]

sol = Solution()
print(sol.isPalindrome("A man a plan a canal Panama"))
print(sol.isPalindrome("Was it a car or a cat I saw?"))