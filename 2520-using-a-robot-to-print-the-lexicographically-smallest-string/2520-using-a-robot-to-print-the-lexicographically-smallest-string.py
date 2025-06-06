

class Solution:
    def robotWithString(self, s: str) -> str:
        count = Counter(s)
        result = []
        stack = []
        min_char = 'a'

        for c in s:
            stack.append(c)
            count[c] -= 1

            # Update the smallest remaining character
            while min_char <= 'z' and count[min_char] == 0:
                min_char = chr(ord(min_char) + 1)

            # Pop from stack while it's optimal
            while stack and stack[-1] <= min_char:
                result.append(stack.pop())

        # Pop any remaining characters
        while stack:
            result.append(stack.pop())

        return ''.join(result)