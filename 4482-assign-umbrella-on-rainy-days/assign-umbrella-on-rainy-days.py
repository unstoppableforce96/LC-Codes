class Solution:
    def assignUmbrella(self, rain: list[int]) -> list[str]:
        alice = bob = 0
        n = len(rain)
        ans = []
        for i in range(n):
            if rain[i]:
                if i + 1 < n and rain[i + 1] == 1:
                    if alice <= bob:
                        alice += 1
                        ans.append('Alice')
                    else:
                        bob += 1
                        ans.append('Bob')
                else:
                    bob += 1
                    ans.append('Bob')
            else:
                ans.append('None')
        return ans
