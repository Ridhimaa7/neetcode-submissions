class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        if len(arr) == 1: return 1
        L = 0
        maxLength = 1
        flipArray = []
        for R in range(len(arr)):
            if R - 1 >= 0:
                if arr[R] > arr[R - 1]:
                    flipArray.append(+1)
                elif arr[R] < arr[R - 1]:
                    flipArray.append(-1)
                else:
                    flipArray.append(0)
                while len(flipArray) >= 1 and (flipArray[-1] == 0 or (len(flipArray) > 1 and flipArray[-1] == flipArray[-2])):
                    flipArray.pop(0)
                    L += 1
                maxLength = max(maxLength , R - L + 1)
            else:
                continue
        return maxLength