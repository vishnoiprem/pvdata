class Solution(object):

    def isScramble(self, s1, s2):

        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        n = len(s1)
        m = len(s2)
        if sorted(s1) != sorted(s2):
            return False
        
        if n < 4 or s1 == s2:
            return True
        
        for i in range(1, n):
            print(i,'i')
            print(s1,s2,s1[:i], s2[:i], s1[i:], s2[i:],'-second-',s1[:i], s2[-i:],s1[i:], s2[:-i])
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            print('prem')
            if self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:-i]):
                return True
        return False
            
if __name__ == "__main__":
    print (Solution().isScramble("rgtae", "great"))
    print (Solution().isScramble("abc", "tt"))
    print("prem"[-1:])