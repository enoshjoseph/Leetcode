class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for op in operations:
            val = val + 1 if "+" in op else val - 1
        return val 
        