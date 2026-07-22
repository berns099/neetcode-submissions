class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        sets = set()
        x = False
        for num in nums:
            if num not in sets:
                sets.add(num)
                x = False
            else:
                x = True
                break
        return x