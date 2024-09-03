class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        if len(nums) == 2:
            return 0 if nums[0] > nums[1] else 1
        if nums[0] > nums[1]:
            return 0
        n = len(nums)
        if nums[-1] > nums[-2]:
            return n - 1
        
        left = 0
        right = n - 1
        mid = 0

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid - 1] and nums[mid] > nums[mid + 1]:
                return mid
            elif nums[mid] < nums[mid - 1]:
                right = mid
            else:
                left = mid
        return mid