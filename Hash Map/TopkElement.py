from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea: create a dictionary to store the frequency of each element in the list
        # then sort the dictionary by the frequency of each element in descending order
        # finally, return the first k elements in the sorted dictionary
        # Solution 1
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        return [sorted_freq[i][0] for i in range(k)]
        # Time complexity: O(nlogn) where n is the number of elements in the list
        # Space complexity: O(n) since we are storing the frequency of each element in a dictionary
        # and the sorted frequency in a list

def main() -> None:
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    
    # expected: [1, 2]
    sol = Solution()
    print(sol.topKFrequent(nums, k))

if __name__ == '__main__':
    main()