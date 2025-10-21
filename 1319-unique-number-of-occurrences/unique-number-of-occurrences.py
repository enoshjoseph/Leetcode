class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = set()
        counter = Counter(arr)
        for i in counter.values():
            if i in seen:
                return False
            else:
                seen.add(i)
        return True
        