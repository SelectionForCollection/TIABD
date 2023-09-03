class Solution:
    def mail_agent(self):
        bd = {}
        n = int(input())
        for _ in range(n):
            buff = input()
            if buff in bd:
                print(buff + str(bd[buff]))
                bd[buff + str(bd[buff])] = 1
                bd[buff] += 1
            else:
                bd[buff] = 1
                print('OK')


if __name__ == '__main__':
    Solution().mail_agent()

