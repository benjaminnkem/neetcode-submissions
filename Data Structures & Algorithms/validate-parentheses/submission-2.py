class Solution:
    def isValid(self, s: str) -> bool:
        open_to_close = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        stack = []
        for bracket in s:
            if bracket not in open_to_close:
                if not stack:
                    return False
                top = stack.pop()

                if open_to_close[top] != bracket:
                    return False
            else:
                stack.append(bracket)
        
        if stack:
            return False
        return True


        
            

