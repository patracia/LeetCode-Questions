class Solution:
    def isPalindrome(self,x:int):
        if x<0 :
            return False
        else:
            rev=0
            main=x
            while x!=0:
                rev=rev*10+x%10
                x=x//10
            if main==rev:
                return True
            else:
                return False

c=Solution()
print(c.isPalindrome(121))
                
            


        
        