class Solution:
    def morze(self, string: str) -> str:
        res = ''
        alphabet = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..',
            'e': '.', 'f': '..-.', 'g': '--.', 'h': '....',
            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
            'm': '--', 'n': '-.', 'o': '---', 'p': '.--.',
            'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
            'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
            'y': '-.--', 'z': '--..'
        }
        for character in string:
            if character == ' ':
                res += '\n'
            else:
                res += alphabet[character.lower()] + ' '
        return res


if __name__ == '__main__':
    string = input()
    print(Solution().morze(string))
