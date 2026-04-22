class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # k= l=left pointer
        k = 1 

        # r=right pointer (scan from 1 to end)
        for r in range(1, len(nums)):
            if nums[r] != nums[r-1]:
                nums[k] = nums[r]
                k += 1
        return k