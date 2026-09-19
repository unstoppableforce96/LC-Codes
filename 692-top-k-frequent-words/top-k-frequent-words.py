class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        words.sort()
        c = Counter(words)
        mc = list(c.most_common(k))
        return [i[0] for i in mc]