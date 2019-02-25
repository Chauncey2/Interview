'''
输入某二叉树的前序遍历和中序遍历的结果，请重建出该二叉树。
假设输入的前序遍历和中序遍历的结果中都不含重复的数字。
例如输入前序遍历序列{1,2,4,7,3,5,6,8}和中序遍历序列{4,7,2,1,5,3,8,6}，则重建二叉树并返回。
'''
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Slotion:

	# 由先序序列和中序序列构造二叉树
	def reConstructBinaryTree(self,pre, tin):

		if not pre or not tin:
			return None

		root=TreeNode(pre.pop(0))
		index=tin.index(root.val)
		root.left=self.reConstructBinaryTree(pre,tin[:index])
		root.right=self.reConstructBinaryTree(pre,tin[index+1:])
		return root
    
    # 先序遍历算法(递归)
	def preOrder(self,TreeNode):
		if not TreeNode:
			return None
		print(TreeNode.val)
		self.preOrder(TreeNode.left)
		self.preOrder(TreeNode.right)

    # 中序遍历算法
	def InOrder(self,TreeNode):
		if not TreeNode:
			return None

		self.InOrder(TreeNode.left)
		print(TreeNode.val)
		self.InOrder(TreeNode.right)

    #后续遍历二叉树
	def postOrder(self,TreeNode):
		if not TreeNode:
			return None

		self.postOrder(TreeNode.left)
		self.postOrder(TreeNode.right)
		print(TreeNode.val)

if __name__ == '__main__':

 	pre=[1,2,4,7,3,5,6,8]
 	tin=[4,7,2,1,5,3,8,6]
 	s=Slotion()
 	root=s.reConstructBinaryTree(pre,tin)
 	# root=reConstructBinaryTree(pre,tin)
 	print(root.val)
 	s.InOrder(root)
 	s.preOrder(root)
 	s.postOrder(root)
    
    





