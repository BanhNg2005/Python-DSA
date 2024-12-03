from typing import List

class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set() # store the numbers that have been seen
        for num in arr:
            if num * 2 in seen or num / 2 in seen: # check if the double or half of the number has been seen
                return True
            seen.add(num) # add the number to the set
        return False # if no such number is found, return False

        # Time complexity: O(n)
        # Space complexity: O(n)

def main() -> None:
    arr = [10,2,5,3]
    # expected: True
    arr1 = [7,1,14,11]
    # expected: True
    arr2 = [3,1,7,11]
    # expected: False
    sol = Solution()
    print(sol.checkIfExist(arr))
    print(sol.checkIfExist(arr1))
    print(sol.checkIfExist(arr2))

if __name__ == '__main__':
    main()