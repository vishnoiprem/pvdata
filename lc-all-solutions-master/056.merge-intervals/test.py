
# Definition for an interval.
class Interval:
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort( key=lambda x: x.start )

        result=[intervals[0]]
        for i in range(1,len(intervals)):
        	prev, current = result[-1], intervals[i]
        	if current.start <= prev.end: 
            		prev.end = max(prev.end, current.end)
        	else:
        		result.append(intervals[i])
        return result
if __name__ == "__main__":
    print (Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)]))