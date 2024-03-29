# Time:  O(n)
# Space: O(k), k is maxWidth.
#
# Given an array of words and a length L, format the text such that
# each line has exactly L characters and is fully (left and right) justified.
# 
# You should pack your words in a greedy approach; that is, pack 
# as many words as you can in each line. Pad extra spaces ' ' 
# when necessary so that each line has exactly L characters.
# 
# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line do not divide evenly between words, 
# the empty slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space
# is inserted between words.
# 
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# 
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.














class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        ans = []
        line = []
        lens = map(len, words)
        idx = 0
        curLen = 0
        while idx < len(words):
            if curLen == 0:
                curLen = lens[idx]
            else:
                curLen += lens[idx] + 1
            line.append(words[idx])
            idx += 1
            if curLen > maxWidth:
                curLen = 0
                line.pop()
                idx -= 1
                if len(line) == 1:
                    ans.append(line[0] + " " * (maxWidth - len(line[0])))
                    line = []
                    continue
                spaces = maxWidth - sum(map(len,line))
                avgSpace = spaces //(len(line) - 1)
                extraSpace = spaces % (len(line) - 1)
                res = ""
                for i in xrange(0, len(line)):
                    res += line[i]
                    if i < len(line) - 1:
                        res += " " * (avgSpace + (extraSpace > 0))
                        extraSpace -= 1
                ans.append(res)
                line = []
            elif idx == len(words):
                res = ""
                for i in xrange(0, len(line)):
                    res += line[i]
                    if i < len(line) - 1:
                        res += " "
                res += " " * (maxWidth - len(res))
                ans.append(res)
        return ans

#if __name__ == "__main__":
#    print (Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))


# Time:  O(n)
# Space: O(k), k is maxWidth.
#
# Given an array of words and a length L, format the text such that
# each line has exactly L characters and is fully (left and right) justified.
# 
# You should pack your words in a greedy approach; that is, pack 
# as many words as you can in each line. Pad extra spaces ' ' 
# when necessary so that each line has exactly L characters.
# 
# Extra spaces between words should be distributed as evenly as possible. 
# If the number of spaces on a line do not divide evenly between words, 
# the empty slots on the left will be assigned more spaces than the slots on the right.
# 
# For the last line of text, it should be left justified and no extra space
# is inserted between words.
# 
# For example,
# words: ["This", "is", "an", "example", "of", "text", "justification."]
# L: 16.
# 
# Return the formatted lines as:
# [
#    "This    is    an",
#    "example  of text",
#    "justification.  "
# ]
# Note: Each word is guaranteed not to exceed L in length.

class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        def addSpaces(i, spaceCnt, maxWidth, is_last):
            if i < spaceCnt:
                # For the last line of text, it should be left justified,
                # and no extra space is inserted between words.
                return 1 if is_last else (maxWidth // spaceCnt) + int(i < maxWidth % spaceCnt)
            return 0

        def connect(words, maxWidth, begin, end, length, is_last):
            s = []  # The extra space O(k) is spent here.
            n = end - begin
            for i in range(n):
                s += words[begin + i],
                s += ' ' * addSpaces(i, n - 1, maxWidth - length, is_last),
            # For only one word in a line.
            line = "".join(s)
            if len(line) < maxWidth:
                line += ' ' * (maxWidth - len(line))
            return line

        res = []
        begin, length = 0, 0
        for i in range(len(words)):
            if length + len(words[i]) + (i - begin) > maxWidth:
                res += connect(words, maxWidth, begin, i, length, False),
                begin, length = i, 0
            length += len(words[i])

        # Last line.
        res += connect(words, maxWidth, begin, len(words), length, True),
        return res


if __name__ == "__main__":
    print (Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))