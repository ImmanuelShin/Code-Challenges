class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        res = [[] for _ in range(numRows)]
        count = 0
        d = "down"
        for c in s:
            res[count].append(c)
            if d == "down":
                if count == numRows - 1:
                    d = "up"
                    count -= 1
                else:
                    count += 1
            elif d == "up":
                if count == 0:
                    d = "down"
                    count += 1
                else:
                    count -= 1

        return "".join([char for row in res for char in row])
            
                    
class FixedMatrixSolution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) == 1 or numRows == 1:
            return s
        m = ((len(s) - 1) // (numRows - max((numRows - 2), 0))) + 1

        matrix = [[None for _ in range(m)] for _ in range(numRows)]
        
        direction = "down"
        count = 1
        x = 0
        y = 0

        for c in s:
            matrix[y][x] = c
            if direction == "down":
                if y == numRows - 1:
                    direction = "up"
                    y -= 1
                    x += 1
                else:
                    y += 1
            elif direction == "up":
                if y == 0:
                    direction = "down"
                    y += 1
                else:
                    y -= 1
                    x += 1
        res = "".join([value for row in matrix for value in row if value is not None])
        return res
            
