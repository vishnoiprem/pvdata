class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        ret = [[0 for j in range(len(B[0]))] for i in range(len(A))]
        print(ret)

        for i, row in enumerate(A):
            print(i,row)
            for k, a in enumerate(row):
                print(k,a)
                if a:
                    for j, b in enumerate(B[k]):
                        print(B[k])
                        print('jb',j,b)
                        if b:
                            ret[i][j]=ret[i][j]+ a * b
        return ret


A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

print(Solution().multiply(A,B))