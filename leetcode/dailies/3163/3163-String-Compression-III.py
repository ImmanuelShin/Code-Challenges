class Solution:
    def compressedString(self, word: str) -> str:
        comp = ""

        count = 1
        n = len(word)
        cur = word[0]

        for i in range(1,n):
            if word[i] == cur and count < 9:
                count += 1
            else:
                comp += str(count) + cur
                cur = word[i]
                count = 1
        comp += str(count) + cur
        return comp
                