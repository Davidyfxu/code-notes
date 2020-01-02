# python代码笔记

#### 列表拷贝

```python
# [26] 删除排序数组中的重复项
#
# @lc code=start
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums[:] = sorted(list(set(nums))) #用nums = sorted(list(set(nums)))为浅拷贝
        return len(nums)
```

深copy：

`A=[1,2,3,4]  or  A=A[:]`

浅copy

`B=A`

浅copy在后面对B操作以后就会影响到A，A的值也会随之改变 

#### 列表逆序切片

`A[start:end:-1] 如A[-1:3:-1]为正确的逆序切片表达，start为开始切片的位置，end为终止位置`

#### 单词一个个分开

`s=123413`

`digits = list(str(s)) `

#### 动态插入

```python
first = 'yifan'
last = 'xu'
# situation 1
msg = first + ' ['+last+'] is a coder.'
#sitution 2
msg = f'{first} [{last}] is a coder.'
```

#### mosh python 笔记

Python title() 方法返回"标题化"的字符串,就是说所有单词都是以大写开始，其余字母均为小写。