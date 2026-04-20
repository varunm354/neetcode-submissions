class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pardict = {')' : '(', '}': '{', ']': '['}

        for c in s:
            if c in pardict:
                if stack == []:
                    return False
                if stack[-1] != pardict[c]:
                    return False

                stack.pop()

            else:
                stack.append(c)

            

        return stack == []