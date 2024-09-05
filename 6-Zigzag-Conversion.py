class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        count = 0
        d = \down\
        for c in s:
            res[count].append(c)
            if d == \down\:
                if count == numRows - 1:
                    d = \up\
                    count -= 1
                else:
                    count += 1
            elif d == \up\:
                if count == 0:
                    d = \down\
                    count += 1
                else:
                    count -= 1

        return \\.join([char for row in res for char in row])
            
                    

