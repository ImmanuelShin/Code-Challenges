class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return None
        ran = []
        prev = nums[0]
        for i in range(len(nums)):
            if i == len(nums) - 1 or nums[i] != (nums[i+1] - 1):
                if prev == nums[i]:
                    ran.append(str(nums[i]))
                else:
                    ran.append(str(prev) + \->\ + str(nums[i]))
                if i < len(nums) - 1:
                    prev = nums[i + 1]
        return ran
