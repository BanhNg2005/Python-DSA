from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        merge = []
        intervals.sort(key = lambda interval: interval[0] )

        for interval in intervals:
            if not merge or merge[-1][1] < interval[0]:
                merge.append(interval)
            else:
                merge[-1] = [merge[-1][0], max(merge[-1][1], interval[1])]
        return merge

def main() -> None:
    intervals = [[1,3],[2,6],[7,9],[8,10]]
    sol = Solution()
    print(sol.merge(intervals))

if __name__ == '__main__':
    main()