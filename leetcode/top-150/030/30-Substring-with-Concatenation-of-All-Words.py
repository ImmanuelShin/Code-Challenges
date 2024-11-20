class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        sorted_words = ''.join(sorted(words))
        len_sort = len(sorted_words)
        len_s = len(s)
        len_word = len(words[0])

        res = []

        for i in range(len_s - len_sort + 1):
            temp = []
            for j in range(i, i + len_sort, len_word):
                temp.append(s[j: j + len_word])
            temp = ''.join(sorted(temp))
            if temp == sorted_words:
                res.append(i)
        return res

            


        