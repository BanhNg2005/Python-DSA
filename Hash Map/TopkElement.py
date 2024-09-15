from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # idea: create a dictionary to store the frequency of each element in the list
        # then sort the dictionary by the frequency of each element in descending order
        # finally, return the first k elements in the sorted dictionary
        # Solution 1
        # freq = {}
        # for num in nums:
        #     if num in freq:
        #         freq[num] += 1
        #     else:
        #         freq[num] = 1
        
        # sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
        # return [sorted_freq[i][0] for i in range(k)]
        # Time complexity: O(nlogn) where n is the number of elements in the list
        # Space complexity: O(n) since we are storing the frequency of each element in a dictionary
        # and the sorted frequency in a list

        # Solution 2
        # Bucket sort
        # we will map the count of each value, keeping a list of frequencies to avoid out-of-bounds 
        # issues with large numbers. we will scan up to size 6, proportional to 
        # the input array, and iterate from maximum to minimum frequency.

        count = {}
        freq = [[] for _ in range(len(nums) + 1)] # freq will be: [[], [], [], [], [], []]

        for n in nums:
            # count the number of times n appears in the list, if found increment by 1, otherwise set to 0
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items(): # count.items() returns a list of tuples containing the key and value
            freq[c].append(n) # at index c, append the value n to the list of frequencies

        res = []
        for i in range (len(freq) - 1, 0, -1): # iterate from the end of the list to the beginning
            for n in freq[i]:
                res.append(n) # append the value n to the result list
                if len(res) == k: # at some point, the result output will have the same size as k because
                    # we are guaranteed to have at least k values in the input array
                    return res
        # Time complexity: O(n) since we have to iterate through the list of frequencies and the list of elements
        # Space complexity: O(n) since we have to count the occurrences of each value in the input array


def main() -> None:
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    
    # expected: [1, 2]
    sol = Solution()
    print(sol.topKFrequent(nums, k))

if __name__ == '__main__':
    main()