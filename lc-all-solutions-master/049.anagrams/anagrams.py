import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        def hash(count):
            p1, p2 = 2903, 29947
            ret = 0
            for c in count:
                ret = ret * p1 + c
                p1 *= p2
            return ret
            
        d = {}
        
        for str in strs:
            count = [0] * 26
            for c in str:
                count[ord(c) - ord('a')] += 1
            key = hash(count)
            if key not in d:
                d[key] = [str]
            else:
                d[key].append(str)
        return [d[k] for k in d]
            
# Time:  O(n * glogg), g is the max size of groups.
# Space: O(n)
#
# Given an array of strings, return all groups of strings that are anagrams.
#
# Note: All inputs will be in lower-case.
#

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagrams_map, result = collections.defaultdict(list), []
        #print(anagrams_map)
        for s in strs:
            sorted_str = ("").join(sorted(s))
            #print(sorted_str)
            anagrams_map[sorted_str].append(s)
            print(anagrams_map)

            
        for anagram in anagrams_map.values():
            #print (anagram)
            #anagram.sort()
            result.append(anagram)
        return result


if __name__ == "__main__":
    a=["eat", "tea", "tan", "ate", "nat", "bat"]
    #result = Solution().groupAnagrams(["cat", "dog", "act", "mac"])
    result = Solution().groupAnagrams(a)

    print (result)