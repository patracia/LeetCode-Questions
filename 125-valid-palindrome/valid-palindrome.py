class Solution:
    def isPalindrome(self, s: str):
        main = ""

        for char in s:
            if char.isalnum():
                main =main+ char.lower()

        return main == main[::-1]
        
        