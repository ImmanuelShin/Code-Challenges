class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[0])
        cur_end = points[0][1]
        count = 1
        for point in points[1:]:
            if point[0] > cur_end:
                count += 1
                cur_end = point[1]
            else:
                cur_end = min(point[1], cur_end)
        return count