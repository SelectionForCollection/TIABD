class Solution:
    def matematicheskie_prikoly(self) -> float:
        arr = []
        arr1 = []
        counter = 0
        while True:
            arr.append(float(input()))
            arr1.append(arr[counter]**2)
            counter += 1
            if sum(arr) == 0.0:
                break
        return sum(arr1)


if __name__ == '__main__':
    print(Solution().matematicheskie_prikoly())
