


class Solution(object):
    def merge(self, nums1, m, nums2, n):
    	end=m+n-1
    	m=m-1
    	n=n-1



    	while end>=0 and m>=0 and n>=0:

    		if nums1[m]>nums2[n]:
    			nums1[end]=nums1[m]
    			m=m-1
    		else:
    			nums1[end]=nums2[n]

    			n=n-1

    		end=end-1

    	while n>=0:
    		nums1[end]=nums2[n]
    		n=n-1
    		end=end-1
    		


    	return nums1




if __name__ == "__main__":
    A = [1, 3, 5, 0, 0, 0, 0]
    B = [2, 4, 6, 7]
    print(Solution().merge(A, 3, B, 4))
    print (A)