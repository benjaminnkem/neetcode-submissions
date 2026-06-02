class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        output: list[int] = []
        for i in range(len(arr)):
            if i == len(arr) - 1:
                output.append(-1)
            else:
                rest = arr[i + 1 : len(arr)]
                highest = sorted(rest, reverse=True)[0]
                output.append(highest)

        return output
