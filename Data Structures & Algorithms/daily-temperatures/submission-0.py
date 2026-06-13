class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # BRUTE FORCE APPROACH

        result = []

        for i in range(len(temperatures)):
            counter = 0
            found_greater = False

            for j in range(i + 1, len(temperatures)):
                counter += 1

                if temperatures[j] > temperatures[i]:
                    found_greater = True
                    break

            if not found_greater:
                counter = 0

            result.append(counter)

        return result
