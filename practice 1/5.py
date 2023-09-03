class Solution:
    def prosto_prikoly(self, a: list, b: list) -> dict:
        super_dict = {}
        for character in sorted(set(b)):
            super_dict[character] = 0
        for i in range(len(b)):
            super_dict[b[i]] += a[i]
        return super_dict


if __name__ == '__main__':
    a = [1, 2, 3, 4, 2, 1, 3, 4, 5, 6, 5, 4, 3, 2]
    b = ['a', 'b', 'c', 'c', 'c', 'b', 'a', 'c', 'a', 'a', 'b', 'c', 'b', 'a']
    print(Solution().prosto_prikoly(a, b), '\n')
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    b = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']
    print(Solution().prosto_prikoly(a, b))
