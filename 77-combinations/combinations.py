class Solution:
    def combine(self, n: int, k: int) -> list[list[int]]:
        result = []
        def generate(value, current):
            if value > n:
                if len(current) == k:
                    result.append(current.copy())
                return
            current.append(value) 
            generate(value + 1, current) # pick

            current.pop() # undo

            generate(value + 1, current)   
        generate(1, [])
        return result
