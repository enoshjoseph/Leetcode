class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for word in strs:
            ls = [0] * 26
            for ch in word:

                idx = ord(ch) - ord('a')
                ls[idx] += 1
            
            dict[tuple(ls)].append(word)
        return list(dict.values())
        