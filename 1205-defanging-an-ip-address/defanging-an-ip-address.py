class Solution:
    def defangIPaddr(self, address: str) -> str:
        arr = []
        for c in address:
            if c == '.':
                arr.append('[.]')
            else:
                arr.append(c)
        
        return ''.join(arr)
        