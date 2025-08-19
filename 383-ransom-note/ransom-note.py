class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        dict = defaultdict(int)
        for ch in magazine:
            dict[ch] += 1
        
        for ch in ransomNote:
            if ch not in dict:
                return False

            dict[ch] -= 1

            if dict[ch] == 0:
                del dict[ch]
        return True
        