class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []
        def generate(index, current):
            if index == len(nums):
                result.append(current.copy())
                return
            
            current.append(nums[index])
            generate(index + 1, current) # pick

            current.pop() # undo

            generate(index + 1, current) # leave
        
        generate(0, [])
        return result