class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(remain,comb,nex):
            if remain == 0:
                res.append(comb.copy())
            else:
                for i in range(nex,n+1):
                    comb.append(i)
                    backtrack(remain-1,comb,i+1)
                    comb.pop()
                    
        backtrack(k,[],1)
        return res