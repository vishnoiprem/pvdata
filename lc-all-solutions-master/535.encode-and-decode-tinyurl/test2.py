#https://www.youtube.com/watch?v=fMZMm_0ZhK4
import random

class Codec:


	def __init__(self):

		self.__random_length=6
		self.__tiny_url="http://tinyurl.com/"
		self.__alphabet="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
		self.__lookup={}


	def enCode(self, longURL):

		


		def getRand():
			rand=""

			for i in range(self.__random_length):
				rand=rand+self.__alphabet[random.randint(0,len(self.__alphabet)-1)]
			return rand



		key=getRand()

		while key in self.__lookup:
			key=getRand()
		self.__lookup[key]=longURL
		return self.__tiny_url+key




	def deCode(self, shortURL):


		return self.__lookup[shortURL[len(self.__tiny_url):]]



if __name__=="__main__":
	print('p')
	ende=Codec()
	longURL="https://leetcode.com/problems/encode-and-decode-tinyurl/description/"
	print(ende.enCode(longURL))
	a=ende.enCode(longURL)
	print(ende.deCode(a))