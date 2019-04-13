class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
            
        d = {1: "", 2: "abc", 3: "def", 4: "ghi", 5: "jkl", 6: "mno", 7: "pqrs", 8: "tuv", 9: "wxyz"}
        
        def dfs(digits, index, path, res, d):
            if index == len(digits):
                res.append("".join(path))
                return 
        
            digit = int(digits[index])
            for c in d.get(digit, []):
                path.append(c)
                dfs(digits, index + 1, path, res, d)
                path.pop()
        
        res = []
        dfs(digits, 0, [], res, d)
        return res

s=Solution()
print(s.letterCombinations(''))

print('Prem')

"""
17. Letter Combinations of a Phone Number


Given a digit string, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below.

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

"""
class Solution1(object):

    def __init__(self):

        self.d = {
            "0": "_",
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

    def letterCombinations(self, digits):

        """
        Explanation:
        Recursively build out a tree structure
        for the string "23" and collect all the paths
        to leaf nodes

        2  -> "abc" , 3 -> "def"

                    ROOT
                /    |     \
            a        b      c
        /   |  \   / | \  / | \
        d   e   f  d  e f d e f

        Time : O(exp)
        Space: O(exp)


        :type digits: str
        :rtype: List[str]
        """
        combinations = []

        def recurse(_digits, acc):
            print('combinations',combinations)
            if not _digits:
                combinations.append(acc)
                return

            first, rest = _digits[0], _digits[1:]

            chars = self.d[first]

            for char in chars:
                print(char,acc,chars)

                recurse(rest, acc + char)

        recurse(digits, '')

        return combinations if len(combinations)>1 else []


r = Solution1()
res = r.letterCombinations('23')
print (res)




                