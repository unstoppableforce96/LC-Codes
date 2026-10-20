class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        result = set()
        candidates.sort()
        def generate(index, current, remaining):
            if remaining == 0:
                result.add(tuple(current.copy()))
                return
            if index == len(candidates) or remaining < 0:
                return
            current.append(candidates[index])
            generate(index + 1, current, remaining - candidates[index])
            current.pop()
            next_index = index + 1
            while next_index < len(candidates) - 1 and candidates[next_index] == candidates[index]:
                next_index += 1
            generate(next_index, current, remaining)
        
        generate(0, [], target)
        return list(result)