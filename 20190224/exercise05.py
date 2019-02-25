'''
用两个栈来实现一个队列，完成队列的Push和Pop操作。 队列中的元素为int类型。
'''

'''
class Solution:

	stack_in=[]
	stack_out=[]
	# 进队操作
	def push(self,node):
		# 若两个栈都为空，则元素进栈stack_in
		if len(self.stack_in)==0 and len(self.stack_out)==0:
			self.stack_in.append(node)
		elif len(self.stack_in)==0 and len(self.stack_out)!=0:
			self.stack_in.append(node)
		elif len(self.stack_in)!=0 and len(self.stack_out)==0:
			self.stack_in.append(node)
		else:
			self.stack_in.append(node)
			
	# 出队操作
	def pop(self):
		if len(self.stack_out)==0 and len(self.stack_in)==0:
			return 
		elif len(self.stack_out)==0 and len(self.stack_in)!=0:

			# 将stack_out栈中的数据全部存储到出栈中
			while len(self.stack_in)!=0:
				self.stack_out.append(self.stack_in.pop())

			return self.stack_out.pop()
		else:
			# print("测试",self.stack_out)
			return self.stack_out.pop()
'''

'''
方法二，更简便
'''
class Solution:
	stack_in=[]
	stack_out=[]

	def push(self,node):
		self.stack_in.append(node)

	def pop(self):
		if len(self.stack_out)==0:
			while len(self.stack_in)!=0:
				self.stack_out.append(self.stack_in.pop())
		return self.stack_out.pop()






if __name__ == '__main__':	

	
	# print(Solution.stack_in)

	for i in range(10):
		Solution().push(i)
	# print(Solution().pop())
	# print('stack_out:',Solution().stack_out)
	# print('stack_in:',Solution().stack_in)

	# print(Solution().pop())
	# print('stack_out:',Solution().stack_out)
	# print('stack_in:',Solution().stack_in)

	for i in range(10,15):
		Solution().push(i)

	print("*"*30)

	for i in range(0,15):
		print(Solution().pop())

	# print(Solution().pop())
	# print('stack_out:',Solution().stack_out)
	# print('stack_in:',Solution().stack_in)
	# print(Solution().pop())

	# print('stack_out:',Solution().stack_out)
	# print('stack_in:',Solution().stack_in)






