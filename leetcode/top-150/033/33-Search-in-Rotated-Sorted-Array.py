class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            if nums[left] == target:
                return left
            if nums[right] == target:
                return right
            mid = (left + right) // 2
            if nums[mid] < target:
                if nums[left] < target and nums[left] > nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                if nums[left] > target and nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                return mid
        return -1