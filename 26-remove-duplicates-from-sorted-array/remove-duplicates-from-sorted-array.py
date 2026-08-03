class Solution:
    def removeDuplicates(self,nums ):
        nums.sort()
        print(nums.sort())
        i=0
        while  i<len(nums)-1:
            if nums[i]==nums[i+1]:
                nums.pop(i+1)
            else:
                i=i+1
        return len(nums)

c=Solution()
print(c.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


        
        