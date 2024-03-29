# Time:  O(n)
# Space: O(1)
#
# Validate if a given string is numeric.
# 
# Some examples:
# "0" => true
# " 0.1 " => true
# "abc" => false
# "1 a" => false
# "2e10" => true
# Note: It is intended for the problem statement to be ambiguous.
# You should gather all requirements up front before implementing one.
#




class States(object):
    def __init__(self):
        self.init = 0
        self.decimal = 1
        self.decpoint = 2
        self.afterdp = 3
        self.e = 4
        self.aftere = 5
        self.sign = 6
        self.nullpoint = 7
        self.esign = 8
        self.afteresign = 9
        
        
class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip()
        states = States()
        state = states.init
        decimals = "01234567890"

        for c in s:
            if state == states.init:
                if c == ".":
                    state = states.nullpoint
                elif c in decimals:
                    state = states.decimal
                elif c in ["+", "-"]:
                    state = states.sign
                else:
                    return False
            elif state == states.sign:
                if c in decimals:
                    state = states.decimal
                elif c == ".":
                    state = states.nullpoint
                else:
                    return False
            elif state == states.esign:
                if c not in decimals:
                    return False
                state = states.afteresign
            elif state == states.afteresign:
                if c not in decimals:
                    return False
            elif state == states.nullpoint:
                if c not in decimals:
                    return False
                state = states.decpoint
            elif state == states.decimal:
                if c in decimals:
                    continue
                elif c == "e":
                    state = states.e
                elif c == ".":
                    state = states.decpoint
                else:
                    return False
            elif state == states.decpoint:
                if c in decimals:
                    state = states.afterdp
                elif c == "e":
                    state = states.e
                else:
                    return False
            elif state == states.afterdp:
                if c in decimals:
                    continue
                elif c == "e":
                    state = states.e
                else:
                    return False
            elif state == states.e:
                if c in decimals:
                    state = states.aftere
                elif c in ["+", "-"]:
                    state = states.esign
                else:
                    return False
            elif state == states.aftere:
                if c not in decimals:
                    return False
            else:
                return False
        return state not in [states.init, states.e, states.nullpoint, states.sign, states.esign]


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        import re
        return bool(re.match("^\s*[\+-]?((\d+(\.\d*)?)|\.\d+)([eE][\+-]?\d+)?\s*$", s))


if __name__ == "__main__":
    print (Solution().isNumber(" 0.1 "))
    print (Solution().isNumber("abc"))
    print (Solution().isNumber("1 a"))
    print (Solution().isNumber("2e10"))
