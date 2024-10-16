class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sorted_intervals = sorted(intervals, key=lambda x: x[0])
        res = []
        temp = None
        for i in range(len(sorted_intervals)):
            if temp is None:
                temp = sorted_intervals[i]
            elif temp[1] >= sorted_intervals[i][0]:
                temp[1] = max(temp[1], sorted_intervals[i][1])
            else:
                res.append(temp)
                temp = sorted_intervals[i]
            if i == len(sorted_intervals) - 1:
                res.append(temp)
        return res
            