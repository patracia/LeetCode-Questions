class Solution:
    def longestPalindrome(self, s: str) -> str:
        # main=""
        m=[]
        large=""
        for i in range(len(s)):
            main=""
            for j in range(i,len(s)):
                main+=str(s[j])
                if main==main[::-1]:
                    m.append(main)
        # for k in range(len(m)):
        #     if len(m[k])<len(m[k+1]):
        #         large=m[k+1]
        #     else:
        #         large=m[k]
        return max(m,key=len)
                    
                
                

                
            

            

        