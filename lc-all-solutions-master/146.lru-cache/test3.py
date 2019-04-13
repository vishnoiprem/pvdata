
import  collections


order_dict=collections.OrderedDict()
d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
d['z']=10

print(collections.OrderedDict(d))


print(order_dict)



class LRUCache(object):


	def __init__(self ,capacity):

		self.cache=collections.OrderedDict()
		self.capacity=capacity


	def put(self , key , val):

		if key in self.cache:
			del self.cache[val]
		elif self.capacity==len(self.cache):
			self.cache.popitem(last=False)
		self.cache[key]=val
		return val

	def get(self, key):

		if not key in self.cache:
			return -1
		val=self.cache[key]
		del self.cache[key]
		self.cache[key]=val






if __name__ == "__main__":
    cache = LRUCache(3)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.put(3, 3)
    print (cache.get(1),'prem')
    cache.put(4, 4)
    print (cache.get(2),'prem')


