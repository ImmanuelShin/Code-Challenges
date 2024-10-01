class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        d = {}
        for x in arr:
            remainder = ((x % k) + k) % k
            if remainder in d:
                d[remainder] += 1
            else:
                d[remainder] = 1
        for x in d:
            if x == 0:
                if d[x] % 2 != 0:
                    return False
            elif k - x in d:
                if d[x] != d[k - x]:
                    return False
            elif d[x] > 0:
                return False
        return True