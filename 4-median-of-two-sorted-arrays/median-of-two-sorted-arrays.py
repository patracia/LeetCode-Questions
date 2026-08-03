class Solution:
    def findMedianSortedArrays(self, n, m) -> float:
        arr = sorted(n + m)
        print(arr)
    
        if len(arr) % 2 == 0:
            return (arr[len(arr) // 2] + arr[len(arr) // 2 -1])/2
        else:
            return arr[len(arr) // 2]


        

        