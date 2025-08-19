class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        seen = set()
        ls = s.split()
        if len(pattern) != len(ls): return False

        for i, ch in enumerate(pattern):
            if ch not in dict:
                if ls[i] in seen:
                    return False
                
                dict[ch] = ls[i]
                seen.add(ls[i])
            else:
                if dict[ch] != ls[i]: return False
        return True

        