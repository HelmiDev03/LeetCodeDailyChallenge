class Solution:
    def compress(self, chars: List[str]) -> int:
        counter = 1
        new_str = ''
        for i in range(1, len(chars)):
            if chars[i - 1] != chars[i]:
                new_str += chars[i - 1]
                if counter > 1:
                    new_str += str(counter)
                counter = 0
            counter += 1

        new_str += chars[-1]
        if counter > 1:
            new_str += str(counter)

        for x in new_str[::-1]:
            chars.insert(0, x)
        return len(new_str)