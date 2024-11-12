from typing import List

class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()  # Sort items based on price, to allow efficient processing with increasing prices.

        # Pair each query with its original index and sort by query price
        queries = sorted([(q, i) for i, q in enumerate(queries)])  # this is called a list comprehension
        result = [0] * len(queries)  # Initialize the result array to store max beauty for each query.

        max_beauty = 0  # Keep track of the maximum beauty seen so far for items within the query price.
        j = 0  # Pointer to iterate through sorted items

        for q, i in queries:
            # Process items with prices <= current query price q
            while j < len(items) and items[j][0] <= q:
                max_beauty = max(max_beauty, items[j][1])  # Update max_beauty if current item has higher beauty
                j += 1  # Move to the next item for further comparison

            # Store the max beauty for the current query's index in the result array
            result[i] = max_beauty

        return result

        # Time complexity: O(Nlogn+Q)
        # Space complexity: O(Q)

def main() -> None:
    items = [[1,2],[3,2],[2,4],[5,6],[3,5]]
    queries = [1,2,3,4,5,6]
    # expected: [2,4,5,5,6,6]
    items1 = [[1,2],[1,2],[1,3],[1,4]]
    queries1 = [1]
    # expected: [4]
    sol = Solution()
    print(sol.maximumBeauty(items, queries))
    print(sol.maximumBeauty(items1, queries1))

if __name__ == '__main__':
    main()