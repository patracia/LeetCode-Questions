class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        
        s.reverse()
        print(s)
        
f=Solution()
f.reverseString(["h","e","l","l","o"])