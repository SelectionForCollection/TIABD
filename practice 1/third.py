class Solution:
    def file_system(self):
        commands = {
            'write': 'w',
            'read': 'r',
            'execute': 'x'
        }
        dfs = {}
        n = int(input())
        for _ in range(n):
            buff = input().split()
            dfs[buff[0]] = buff[1:]
        m = int(input())
        for _ in range(m):
            buff = input().split()
            if commands[buff[0]] in dfs[buff[1]]:
                print('OK')
            else:
                print('Access denied')


if __name__ == '__main__':
    Solution().file_system()
