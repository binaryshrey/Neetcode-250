# https://neetcode.io/problems/duplicate-integer

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = set()
        for i in range(len(nums)):
            arr.add(nums[i])

        return len(arr) != len(nums)