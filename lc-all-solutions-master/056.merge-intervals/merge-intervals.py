# Definition for an interval.
class Interval(object):
     def __init__(self, s=0, e=0):
         self.start = s
         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        ans = []
        for intv in sorted(intervals, key=lambda x:x.start):
            #print(intv)
            if ans and ans[-1].end >= intv.start:
                ans[-1].end = max(ans[-1].end, intv.end)
            else:
                ans = ans+intv,
        return ans

class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e
        
    def __repr__(self):
        return "[{}, {}]".format(self.start, self.end)


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if not intervals:
            return intervals
        #print('prem',intervals)
        intervals.sort(key=lambda x: x.start)
        #print('prem',intervals)
        result = [intervals[0]]
        #print(result)
        for i in range(1, len(intervals)):
            prev, current = result[-1], intervals[i]
            if current.start <= prev.end: 
                prev.end = max(prev.end, current.end)
            else:
                result.append(current)
            #print('result',result)
        return result


if __name__ == "__main__":
    print (Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15,18)]))