class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxim = float('-inf')
        cur = 0
        for x in nums:
            cur = max(x, cur + x)
            maxim = max(maxim, cur)
        return maxim