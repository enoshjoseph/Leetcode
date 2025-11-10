class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        listword1 = list(word1)
        listword2 = list(word2)
        N = len(listword1)
        i = j = 0

        o = []
        while i < len(listword1) or j < len(listword2):
            if i < len(listword1):
                o.append(listword1[i])
                i += 1
            
            if j < len(listword2):
                o.append(listword2[j])
                j += 1 
        return ''.join(o)

        