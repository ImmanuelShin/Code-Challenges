class Solution:
    def rob(self, nums: List[int]) -> int:
        back, furtherback = 0, 0
        for num in nums:
            temp = back
            print(num)
            back = max(furtherback + num, back)
            print(furtherback, temp, back)
            furtherback = temp

        return back