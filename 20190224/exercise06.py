'''
把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。 
输入一个非减排序的数组的一个旋转，输出旋转数组的最小元素。 
例如数组{3,4,5,1,2}为{1,2,3,4,5}的一个旋转，该数组的最小值为1。 
NOTE：给出的所有元素都大于0，若数组大小为0，请返回0。
'''

'''
方法一，直接调用内建函min，返回数组最小值
'''
class Solution:
	def minNumberInRotateArray(self, rotateArray):
		if len(rotateArray)==0:
			return 0
		return min(rotateArray)

'''
方法二，遍历，比较
'''
class Solution2:

	def minNumberInRotateArray(self,rotateArray):

		if len(rotateArray)==0:
			return 0

		min_num=float('Inf')  #定义一个无穷大的数

		for i in rotateArray:
			if i<min_num:
				min_num=i
		return min_num


		



if __name__ == '__main__':

	rotateArray=[3,4,5,1,2]
	s=Solution()
	min_num=s.minNumberInRotateArray(rotateArray)
	print(min_num)

	s2=Solution()
	min_num2=s2.minNumberInRotateArray(rotateArray)
	print(min_num2)