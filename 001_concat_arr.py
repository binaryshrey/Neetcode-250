# https://leetcode.com/problems/concatenation-of-array/submissions/1599394737/

class Solution(object):
    def getConcatenation(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums.extend(nums)
        return nums
        