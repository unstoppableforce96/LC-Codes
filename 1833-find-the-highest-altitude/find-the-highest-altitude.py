class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        return max(list(itertools.accumulate(gain, initial=0)))