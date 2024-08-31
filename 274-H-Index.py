class Solution:
    def hIndex(self, citations: List[int]) -> int:
        h = len(citations)
        citations.sort()
        for x in citations:
            if x < h:
                h -= 1
        return h