from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        # sort the intervals and take the key of the first element of interval
        intervals.sort(key = lambda interval: interval[0] )

        for interval in intervals: # iterate each interval in the list of intervals
            # not yet merged or the end of the last interval is less than the start of the current interval
            if not merge or merge[-1][1] < interval[0]: 
                merge.append(interval)
            else:
                # update the last interval in the merge list to extend its end to the maximum end value
                # between the last interval's end and the current interval's end
                merge[-1] = [merge[-1][0], max(merge[-1][1], interval[1])] 
        return merge
        # Time complexity: O(nlogn) where n is the number of intervals
        # Space complexity: O(n) where n is the number of intervals

def main() -> None:
    intervals = [[2,6],[1,3],[7,9],[8,10]]
    sol = Solution()
    print(sol.merge(intervals))

if __name__ == '__main__':
    main()

# Output: [[1, 6], [7, 10]]