
import collections 


class Solution(object):

	def groupAnagrams(self,stsr):

		defult_dict=collections.defaultdict(list)
		res=[]


		for st in stsr:
			sorteds="".join(sorted(st))
			print(sorteds)
			defult_dict[sorteds].append(st)
		
		for i in defult_dict.values():
			res.append(i)
		return res

if __name__ == "__main__":
    a=["eat", "tea", "tan", "ate", "nat", "bat"]
    #result = Solution().groupAnagrams(["cat", "dog", "act", "mac"])
    result = Solution().groupAnagrams(a)

    print (result)