class Solution:
    def canChange(self, start: str, target: str) -> bool:
        i, j = 0, 0

        while i < len(start) and j < len(target):
            if start[i] == '_':  # we want to ignore the underscore
                i += 1
            elif target[j] == '_':  # same for target
                j += 1
            elif start[i] != target[j]:  # mismatch case
                return False
            # case L
            elif start[i] == 'L' and target[j] == 'L':
                if i < j:  # L cant move right
                    return False
                i += 1
                j += 1
            # case R
            elif start[i] == 'R' and target[j] == 'R':
                if i > j:  # R cant move left
                    return False
                i += 1
                j += 1

        # check the remaining characters in both strings if they are underscores
        while i < len(start):
            if start[i] != '_':
                return False
            i += 1
        while j < len(target):
            if target[j] != '_':
                return False
            j += 1

        return True

        # Time complexity: O(n)
        # Space complexity: O(1)

def main() -> None:
    start = "_L__R__R_"
    target = "L______RR"
    # expected: True
    start1 = "R_L_"
    target1 = "__LR"
    # expected: False
    start2 = "_R"
    target2 = "R_"
    # expected: False
    sol = Solution()
    print(sol.canChange(start, target))
    print(sol.canChange(start1, target1))
    print(sol.canChange(start2, target2))

if __name__ == '__main__':
    main()