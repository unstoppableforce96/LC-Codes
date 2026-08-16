class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Map -> magazine
        d = {}
        for i in magazine:
            if i in d.keys():
                d[i] += 1
            else:
                d[i] = 1
        print(d)
        for i in ransomNote:
            if i not in d.keys():
                return False
            else:
                if d[i] > 0:
                    d[i] -= 1
                else:
                    return False
        return True
