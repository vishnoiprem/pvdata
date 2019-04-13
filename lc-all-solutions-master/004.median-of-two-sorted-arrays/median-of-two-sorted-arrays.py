class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = sorted((nums1, nums2), key=len)
        m, n = len(a), len(b)
        after = (m + n - 1) / 2
        lo, hi = 0, m
        while lo < hi:
            i = (lo + hi) / 2
            if after-i-1 < 0 or a[i] >= b[after-i-1]:
                hi = i
            else:
                lo = i + 1
        i = lo
        nextfew = sorted(a[i:i+2] + b[after-i:after-i+2])
        return (nextfew[0] + nextfew[1 - (m+n)%2]) / 2.0
                

    def findMedian(self,num1,num2):
        sum_ab=sorted(num1+num2)
        print(sum_ab)
        len_ab=len(sum_ab)
        if len_ab%2==1:
            return sum_ab[len_ab//2]
        else:
            return (sum_ab[len_ab//2-1]+sum_ab[len_ab//2])/2.0


s=Solution()
nums1 = [1, 2]
nums2 = [3, 4]

print(s.findMedian(nums1,nums2))