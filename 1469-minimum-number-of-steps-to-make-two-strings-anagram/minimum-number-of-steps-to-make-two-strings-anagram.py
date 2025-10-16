class Solution:
    def minSteps(self, s: str, t: str) -> int:
        dicts = Counter(s)
        dictt = Counter(t)
        
        diff = dicts - dictt
        return sum(diff.values())
            
            
        