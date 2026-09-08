class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        running_sum = 0
        for i in operations:
            if i != 'C' and i != '+' and i != 'D':
                stack.append(int(i))
                running_sum += stack[-1]
            elif i == 'C':
                running_sum -= stack.pop()
            elif i == 'D':
                stack.append(stack[-1] * 2)
                running_sum += stack[-1]
            else:
                stack.append(stack[-1] + stack[-2])
                running_sum += stack[-1]
        return running_sum