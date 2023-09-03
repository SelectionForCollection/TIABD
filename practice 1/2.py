class Solution:
    def calculate(self, string: str) -> float:
        try:
            arr = list(string.split())
            arr[0] = float(arr[0])
            arr[2] = float(arr[2])
            match arr[1]:
                case '+':
                    return arr[0] + arr[2]
                case '-':
                    return arr[0] - arr[2]
                case '/':
                    return arr[0] / arr[2]
                case '//':
                    return arr[0] // arr[2]
                case '**':
                    return arr[0] ** arr[2]
        except Exception:
            arr = list(string.split('('))
            arr[1] = int(arr[1][:-1])
            match arr[0]:
                case 'abs':
                    return abs(arr[1])


if __name__ == '__main__':
    for _ in range(6):
        string = input('Введите выражение - ')
        print(Solution().calculate(string))
