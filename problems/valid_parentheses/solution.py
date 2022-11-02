class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == "(" or ch == "[" or ch == "{":
                stack.append(ch)
            else:
                if len(stack) == 0:
                    return False
                top_item = stack.pop()
                if ch == ")" and top_item != "(" or \
                ch == "}" and top_item != "{" or \
                    ch == "]" and top_item != "[":
                    return False

        if len(stack) > 0:
            return False
        return True