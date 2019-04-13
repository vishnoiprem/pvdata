class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        d = {}
        s3 = list(s3)
        if len(s1) + len(s2) != len(s3):
            return False
        def dfs(s1, i, s2, j, d, path, s3):
            if (i, j) in d:
                return d[(i, j)]
            
            if path == s3:
                return True
            
            if i < len(s1):
                if s3[i + j] == s1[i]:
                    path.append(s1[i])
                    if dfs(s1, i + 1, s2, j, d, path, s3):
                        return True
                    path.pop()
                    d[(i+1, j)] = False
            
            if j < len(s2):
                if s3[i + j] == s2[j]:
                    path.append(s2[j])
                    if dfs(s1, i, s2, j + 1, d, path, s3):
                        return True
                    path.pop()
                    d[(i, j+1)] = False

            
            return False
            
        return dfs(s1, 0, s2, 0, d, [], s3)

r = Solution()
res = r.isInterleave('abc', 'ijk', 'aadbbcbcac')
print (res)


class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        def f(first, second, third):

            if not first and not second:
                return bool(third)


            word = first if first else second

            copy = list(third)
            isFirst = bool(first)

            first_element, rest = word[0], word[1:]

            for index, letter in enumerate(copy):

                print (letter, first_element)
                if letter == first_element:

                    del copy[index]

                    if isFirst:
                        return f(rest, second, copy)
                    else:
                        return f(None, rest, copy)

            return False

        return f(s1, s2, list(s3))

r = Solution()
res = r.isInterleave('abc', 'ijk', 'aadbbcbcac')
print (res)


class Solution:

    # @return a boolean
    def isInterleave(self, s1, s2, s3):
        len1 = len(s1)
        len2 = len(s2)
        len3 = len(s3)

        if len1 + len2 != len3:
            return False
        if 0 == len1:
            return s2 == s3
        if 0 == len2:
            return s1 == s3

        row1 = [False for col in range(len2 + 1)]
        row1[0] = True
        for i in range(1, len2 + 1):
            row1[i] = ( row1[i - 1] and (s2[i - 1] == s3[i - 1]))

        row2 = [False for col in range(len2 + 1)]

        for m in range(1, len1 + 1):
            row2[0] = (row1[0] and (s1[m - 1] == s3[m - 1]))
            for n in range(1, len2 + 1):
                k = m + n - 1
                # why and ? because [m, n] maybe come from up or left, one of the two is the right source.
                row2[n] = (s1[m - 1] == s3[k] and row1[n]) or (s2[n - 1] == s3[k] and row2[n - 1])
            row1, row2 = row2, row1

        return row1[len2]



if __name__ == "__main__":
    print (Solution().isInterleave("a", "", "a"))
    print (Solution().isInterleave("aabcc", "dbbca", "aadbbcbcac"))
    print (Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))
