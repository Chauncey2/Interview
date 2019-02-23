'''
在一个二维数组中（每个一维数组的长度相同），
每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。
请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。
'''

Mylist=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
    [13,14,15,16]
]

'''
方法一：数组是有序的，可以暴力破解，嵌套for循环遍历，但是时间复杂度为O(n^2)
'''
# def Find(target,list):
#     if list is None:    # 如果数组为空，则返回
#         return
#     for item in list:
#         for i in item:
#             if target ==i:
#                 return True
#     return  False

'''
方法二：数组有序，从target与数组最后一行的第一个元素比较，
若target比该元素大，则向左比较（j+1），若target比该元素小，则向上比较（i-1）
该方法时间复杂度为O(n)
'''
def Find(target,array):
    if array is None:
        return

    row_num=array.__len__() -1     #获取行数
    col_num=array[0].__len__() -1  #获取列数

    i=row_num
    j=0
    while j<=col_num and i>=0:
        if target==array[i][j]:
            return True
        if target>array[i][j]:
            j+=1
        elif target<array[i][j]:
            i-=1
    return False

if __name__ == '__main__':


    print(Find(13,Mylist))

