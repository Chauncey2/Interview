'''
请你输出斐波那契数列的第n项（从0开始，第0项为0）。
n<=39
'''
class Solution:

	def Fibonacci(self,n):
		
		if n==1:
			return 1
		a,b=1,0
		num=0
		while n!=0:
			num=a+b
			a,b=b,a+b
			n-=1
		return num



		

if __name__ == '__main__':
	s=Solution()
	print(s.Fibonacci(8))
	
