class Solution(object):



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
        :type digits: str
        :rtype: List[str]
        """
    


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

        """

        combinations = []
        def dfs(_digits,acc):

        	if not _digits:
        		combinations.append(acc)
        		return 


        	first, rest = _digits[0], _digits[1:]

        	print(first,rest,'rest')
        	char=self.d[first]

        	for i in char:
        		print(acc+i)
        		dfs(rest, acc+i)
        dfs(digits,'')
        return combinations if len(combinations)>1 else []

print(Solution().letterCombinations("23"))



