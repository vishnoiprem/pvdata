


class ListNode(object):

	def __init__(self,x):
		self.val=x
		self.next=None




class Solution(object):

	def linkedlistPrint(self,node):

		while node:
			print(node.val)
			node=node.next

	def addLinkedList(self,n1,n2):
		carry=0
		p=dummpy=ListNode(-1)
		while n1 and n2:
			p.next=ListNode(n1.val+n2.val+carry)
			carry=p.next.val//10
			p.next.val=p.next.val%10


			p=p.next

			n1=n1.next
			n2=n2.next
			#print(p.val)

		res=n1 or n2

		while res:
			p.next=ListNode(res.val+carry)
			carry=p.next.val//10
			p.next.val=p.next.val%10


			p=p.next

			res=res.next
			#print(p.val)


		if carry:
			p.next=ListNode(1)
		return dummpy.next

		 

a=ListNode(1)
b=ListNode(2)
c=ListNode(3)
d=ListNode(4)
e=ListNode(1)

a.next=b
b.next=c
c.next=d
d.next=e



a1=ListNode(5)
b1=ListNode(6)
c1=ListNode(7)
d1=ListNode(8)

a1.next=b1
b1.next=c1
c1.next=d1




#print(Solution().linkedlistPrint(a))

#print(Solution().linkedlistPrint(a1))


l=Solution().addLinkedList(a,a1)
#rint('l',Solution().linkedlistPrint(l))






def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(len(A)):
        B.append([0] * n)
        print(B)
        for j in range(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B


A=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]


B = performOps(A)

print(B)
for i in range(len(B)):
    for j in range(len(B[i])):
        print (B[i][j])



Input =[1,2, 2,3,1]
Output =3
ans=Input[0]
for i in range(1,len(Input)):
	ans=ans^ Input[i]
	print(ans,Input[i])
print(ans)


class Solution:
    # @param A : integer
    # @param B : integer
    # @return an integer
    def gcd(self, A, B):

        while B!=0:
            A,B=B,A%B
            print(A,B)
        return A

print(Solution().gcd(6,9))



A=[1, 2, 3, 4]


n=len(A)
i=0


def swap(a,b):
	temp=A[a]
	A[a]=A[b]
	A[b]=temp

while i<=n-2:

	swap(i,i+1)

	i=i+2
print(A)

