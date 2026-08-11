class Solution:

    def encode(self, strs: List[str]) -> str:
        enc_str = ''
        for i in strs:
            enc_str += str(len(i)) + '#' + i
        return enc_str


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):

            # Find the '#' separating length and string
            j = i

            while s[j] != '#':
                j += 1

            # Get length
            length = int(s[i:j])

            # Move past '#'
            j += 1

            # Extract the actual string
            res.append(s[j : j + length])

            # Move to the beginning of next encoded string
            i = j + length

        return res