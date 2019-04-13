class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        start, end = 0, len(s) - 1
        while start < end:
            if not s[start].isalnum():
                start += 1
                continue
            if not s[end].isalnum():
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True
        

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
            
        s_lower = s.lower()
        print(s_lower)
        all_letters = set("Thequickbrownfoxjumpsoverthelazydog0123456789".lower())
        print(all_letters)
        s_prime = ''.join([x for x in s_lower if x in all_letters])
        print(s_prime)
            
        return s_prime == s_prime[::-1]
a="A man, a plan, a canal: Panama"
print(Solution().isPalindrome(a))