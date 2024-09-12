class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        letters = set(allowed)
        total = 0
        for word in words:
            for letter in word:
                if letter not in letters:
                    total -=1
                    break
            total += 1
        return total
                