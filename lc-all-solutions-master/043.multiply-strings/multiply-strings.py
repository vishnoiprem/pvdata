class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = [0] * (len(num1) + len(num2))
        print(ans)

        for i, n1 in enumerate(reversed(num1)):
            for j, n2 in enumerate(reversed(num2)):
                print(n1,n2)
                ans[i + j] += int(n1) * int(n2)
                ans[i + j + 1] += ans[i + j] // 10
                ans[i + j] %= 10
                print(ans)
        print(ans)
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()
        return "".join(map(str, ans[::-1]))


print(Solution().multiply("123","987"))


# Time:  O(m * n)
# Space: O(m + n)
# Using built-in bignum solution.
class Solution2(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        return str(int(num1) * int(num2))


if __name__ == "__main__":
    print (Solution2().multiply("123", "1000"))