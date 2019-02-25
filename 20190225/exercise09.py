'''
一只青蛙一次可以跳上1级台阶，也可以跳上2级……它也可以跳上n级。
求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''
class Solution:
	def jumpFloorII(self, number):
		if number==1:
			return 1
		if number==2:
			return 2
		sum_type=0
		a=1
		b=1
		Fobi_list=[]
		for i in range(number):
			a,b=b,a+b
			if i <=1:				
				Fobi_list.append(a)
			else:
				Fobi_list.append(sum(Fobi_list)+1)
		return Fobi_list[-1]


if __name__ == '__main__':
	s=Solution()

	print(s.jumpFloorII(5))