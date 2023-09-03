class Solution:
    def matematicheskie_prikoly_2_0(self, n: int) -> list:
        arr = []
        counter = 0
        for i in range(1, n):
            for j in range(i):
                if counter == n:
                    return arr
                arr.append(i)
                counter += 1


if __name__ == '__main__':
    n = int(input())
    print(*Solution().matematicheskie_prikoly_2_0(n))
