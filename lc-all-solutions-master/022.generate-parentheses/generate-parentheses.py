class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def dfs(left, path, res, n):
            if len(path) == 2 * n:
                if left == 0:
                    res.append("".join(path))
                return
            
            if left < n:
                path.append("(")
                dfs(left + 1, path, res, n)
                path.pop()
            if left > 0:
                path.append(")")
                dfs(left - 1, path, res, n)
                path.pop()
            
        res = []
        dfs(0, [], res, n)
        return res

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def sub(n, acc):

            if n == 1:
                return acc
            else:
                print ('n', n)
                new = []
                for item in acc:
                    print(item)
                    new.append('(' + item + ')')
                    new.append('()' + item)
                    new.append(item + '()')
                    print('new',new,new + acc)
                return sub(n - 1, new + acc)

        res = set(sub(n, ['()']))
        print(res)
        return [x for x in res if x.count('(') == n]

r = Solution()

x = r.generateParenthesis(3)
print (x)