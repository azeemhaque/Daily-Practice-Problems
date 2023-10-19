class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def remove_char(s):
            stack = []
            for char in s:
                if char == "#" and stack:
                    stack.pop()
                elif char != "#":
                    stack.append(char)
            return stack
        return remove_char(s) == remove_char(t)
            