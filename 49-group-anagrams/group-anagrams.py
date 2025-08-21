class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = defaultdict(list)

        for word in strs:
            len = [0] * 26

            for ch in word:
                idx = ord(ch) - ord('a')

                len[idx]+= 1
            dict[tuple(len)].append(word)
        return list(dict.values())
        