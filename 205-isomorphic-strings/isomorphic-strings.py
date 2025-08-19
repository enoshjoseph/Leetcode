class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dict = {}
        seen = set()
        for i, ch in enumerate(s):
            if s[i] not in dict:
                if t[i] in seen:
                    return False
                dict[ch] = t[i]
                seen.add(t[i])

            else:
                if dict[ch] != t[i]: return False
        return True
        