class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            cursum = numbers[left] + numbers[right]

            if cursum == target:
                return [left + 1, right + 1]
            elif cursum > target:
                right -= 1
            else:
                left += 1
                