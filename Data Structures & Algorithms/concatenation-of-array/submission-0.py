class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i = 0
        ans = [0] * (2 * n)
        while i < (2*n): 
            if i < n:  
                ans[i] = nums[i]
                i += 1
            else:
                ans[i] = nums[i-n]
                i+=1
        return ans
