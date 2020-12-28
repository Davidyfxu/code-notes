# 算法课程笔记--Leetcode

## 1.  数组&链表
### 1.1 反转链表 206

```python
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        cur,prev = head,None

        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
```

### 1.2  判断是否有环 141/142

设置快慢指正

```python
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast, slow = head, head
        if not fast:
            return False
        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False
```



## 2. 堆栈&队列

### 2.1 判断括号字符串是否有效 20

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict_map = {')': '(', ']': '[', '}': '{'}

        for i in s:
            if i not in dict_map:
                stack.append(i)
            elif not stack or dict_map[i] != stack.pop():
                return False

        return not stack 
```

### 2.2 用队列实现栈 255

### 2.3 用栈实现队列 232

```python
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack1 = []
        self.stack2 = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.stack1.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        else:
            return self.stack2.pop()
        return self.stack2.pop()

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        else:
            return self.stack2[-1]

        return self.stack2[-1]

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return len(self.stack1) == 0 and len(self.stack2) == 0
```



## 3. 优先队列



## 4. 哈希表

### 4.1 有效的字母异位词 242

```python
#方法一： Map 哈希表法
def isAnagram(self, s: str, t: str) -> bool:
    dict1, dict2 = {}, {}
    for i in s:
        dict1[i] = dict1.get(i,0) + 1
    for i in t:
        dict2[i] = dict2.get(i,0) + 1
    return dict1 == dict2

#方法二 映射法————数组实现普通哈希表
def isAnagram(self, s: str, t: str) -> bool:
    dict1, dict2 = [0]*26, [0]*26
    for i in s:
        dict1[ord(i)-ord('a')] += 1
    for i in t:
        dict2[ord(i)-ord('a')] += 1
    return dict1 == dict2

#方法三 骚操作————排序法
def isAnagram(self, s: str, t: str) -> bool:
    return sorted(s) == sorted(t)
```

### 4.2  两数之和 1

```python
def twoSum(self, nums: List[int], target: int) -> List[int]:
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[target-nums[i]] = i
        else:
            return dic[nums[i]], i
```

### 4.3  三数之和 15,18

```python
#方法一：暴力法

#方法二：c=-(a+b)set法查询
def threeSum(self, nums: List[int]) -> List[List[int]]:
    if len(nums) < 3:
        return []
    nums.sort()
    res = set()
    for i, v in enumerate(nums[:-2]):
        # 如果v值与nums[i-1]一样，则下一个循环的结果必然一样，不用再做这样一次的循环
        if i >= 1 and v == nums[i-1]:
            continue

        # 同2数之和的方法
        dic = {}
        for x in nums[i+1:]:
            if x not in dic:
                dic[-x-v] = 1
            else:
                res.add((v, -x-v, x))
    return list(map(list, res))

#方法三：sort+find  不如上面快？？？？？
#若 a+b+c>0, c左移; 若 a+b+c<0，C右移  两边夹，逼近0
def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()
    for i in range(len(nums)-1):
        if i >= 1 and nums[i] == nums[i-1]:
            continue

        l, r = i+1, len(nums)-1
        while l < r:
            s = nums[i]+nums[l]+nums[r]
            if s > 0:
                r -= 1
            elif s < 0:
                l += 1
            else:
                res.append((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l, r = l+1, r-1
    return res
```



## 5. 树&二叉树&二叉搜索树

### 5.1  验证二叉搜索树 98

```python
def isValidBST(self, root: TreeNode) -> bool:
    # 方法一 利用中序遍历，获得升序列表
    inorder = self.Inorder(root)
    return inorder == list(sorted(set(inorder)))

    def Inorder(self, root):
        if root is None:
            return []
        return self.Inorder(root.left) + [root.val] + self.Inorder(root.right)
    
	# 方法二 递归，左子树的最大值<根值<右子树的最小值
    def helper(root, Min=float('-inf'), Max=float('inf')):
        if root is None:
            return True

        if root.val <= Min or root.val >= Max:
            return False

        if not helper(root.left, Min, root.val):
            return False
        if not helper(root.right, root.val, Max):
            return False

        return True
    return helper(root)
```

### 5.2  二叉树 & 二叉搜索树的最近公共祖先 235/236

```python
# 二叉树
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None or root == p or root == q:
        return root
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)

    if left == None:
        return right
    else:
        return left if right == None else root
        
# 二叉搜索树
def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if root is None:
        return []
    while root:
        if root.val > p.val and root.val > q.val:
            root = root.left
        elif root.val < p.val and root.val < q.val:
            root = root.right
        else:
            return root
```



## 6. 二叉树遍历

```python
# 前序遍历————根左右
def preorder(self, root):
    if root:
        self.traverse_path.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

# 中序遍历————左根右
def inorder(self, root):
    if root:
        self.inorder(root.left)
        self.traverse_path.append(root.val)
        self.inorder(root.right)

# 后序遍历————左右根
def postorder(self, root):
    if root:
        self.postorder(root.left)
        self.postorder(root.right)
        self.traverse_path.append(root.val)
```



## 7. 递归&分治

```python
'''递归————自身调用自身'''
def recursion(level, param1, param2, ...):
    # recursion terminator  递归终止条件
    if level > MAX_LEVEL:
        print_result
        return
    
    # process logic in current level  数据处理
    process_data(level, data, ...)
	
    # drill down
    self.recursion(level+1, p1) # process后参数变成p1
    
    # reverse the current level status if needed  
    reverse_state(level)
    
'''分治'''
def divide_conquer(problem, param1, param2, ...):
    # recursion terminator
    if problem is None:
        print_result
        return
    
    # process data
    data = prepare_data(problem)
    subproblem = split_problem(problem, data)
    
    # conquer subproblems
    subresult1 = self.divide_conquer(subproblems[0], p1, ...)
    subresult2 = self.divide_conquer(subproblems[1], p1, ...)
    subresult3 = self.divide_conquer(subproblems[2], p1, ...)
    ...
    
    # proces and generate the final result
    result = process_result(subresult1, subresult2, subresult3, ...)
```

### 7.1  Pow(x,n) 50

```python
def myPow(self, x: float, n: int) -> float:
    # 方法二 分治算法
    if n == 0:
        return 1
    if n < 0:
        n, x = -n, 1/x
    if n % 2 == 1:
        return x*self.myPow(x, n-1)
    return self.myPow(x*x, n/2)

    # 方法三 位运算+分治算法 速度最快
    if n == 0:
        return 1
    if n < 0:
        n, x = -n, 1/x
    result = 1
    while n:
        if n & 1:
            result *= x
        x *= x
        n >>= 1
    return result
```

### 7.2  求众数 169

```python
def majorityElement(self, nums: List[int]) -> int:
    # 暴力法 -时间超出
    n = len(nums)
    for num in nums:
        if nums.count(num) >= n/2:
            return num
    return 0

    # Map法
    dic = {}
    for num in nums:
        if num not in dic:
            dic[num] = 1
        dic[num] += 1
    return max(dic, key=dic.get)

    # sort --最快
    return sorted(nums)[len(nums)//2]

    # 分治算法 ——效率低
    def helper(lo, hi):
        if lo == hi:
            return nums[lo]
        mid = (hi-lo)//2 + lo

        left = helper(lo, mid)
        right = helper(mid+1, hi)

        if left == right:
            return left
		
        # 在整个list上做计数统计
        left_count = sum(1 for i in range(lo, hi+1)
                            if nums[i] == left)
        right_count = sum(1 for i in range(lo, hi+1)
                            if nums[i] == right)

        return left if left_count > right_count else right

    return helper(0, len(nums)-1)
```



## 8. BFS

```python
visited = set()
def BFS(graph, start, end):
    queue = []
    queue.append(start)
    visited.add(start)
    while queue:
        node = queue.pop()
        visited.add(node) # 标记已经访问过
        
        process(node)
        nodes = generate_related_nodes(node) # 节点的后继节点若未被访问过则取出
        queue.push(nodes)
    # other processing work
    ''''''
```



## 9. DFS

```python
visited = set()
def DFS(node, visited):
    visited.add(node)
    # process current node here
    ''''''
    for next_node in node.children():
        if next_node not in visited:
            DFS(next_node, visited)
  

'''了解即可，多用递归写法写DFS'''
def DFS(self, tree):
    if tree.root is None:
        return []
    
    visited, stack = set(), [tree.root]
    while stack:
        node = stack.pop()
        visited.add(node) # 标记已经访问过
        
        process(node)
        nodes = generate_related_nodes(node) # 节点的后继节点若未被访问过则取出
        stack.push(nodes)
    # other processing work
    ''''''
```

### 9.1  二叉树层次遍历 102

```python
'''BFS法'''
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    result = []
    queue = collections.deque()
    queue.append(root)
    
    # visited = set(root)
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
                
        result.append(current_level)
    return result


'''DFS法'''
def levelOrder(self, root: TreeNode) -> List[List[int]]:
    if not root:
        return []

    self.result = []
    self._dfs(root, 0)
    return self.result


def _dfs(self, node, level):
    if not node:
        return

    if len(self.result) < level+1:
        self.result.append([])

    self.result[level].append(node.val)

    self._dfs(node.left, level+1)
    self._dfs(node.right, level+1)
```

### 9.2  二叉树的最大和最小深度 104/111

```python
# 判断第一个和最后一个到的叶子节点的深度

# 找最大深度
def maxDepth(self, root):
    if not root:
        return 0
    return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# 找最小深度
def minDepth(self, root):
    if not root:
        return 0
    if not root.left:
        return 1 + self.minDepth(root.right)
    if not root.right:
        return 1 + self.minDepth(root.left)
    
    # divide and conquer
    leftMinDepth = self.minDepth(root.left)
    rightMinDepth = self.minDepth(root.right)
    
    # process subproblems' results
    result = 1 + min(leftMinDepth, rightMinDepth)
    
    return result
```

### 9.3  生成有效括号组合 22

```python
def generateParenthesis(self, n: int) -> List[str]:
    self.list = []
    self._gen(0, 0, n, "")
    return self.list

def _gen(self, left, right, n, result):
    if left == n and right == n:
        return self.list.append(result)
    if left < n:
        self._gen(left+1, right, n, result+'(')
    if left > right and right < n:
        self._gen(left, right+1, n, result+')') 
```



## 10. 二分查找

```python
def binarySearch(ls, target):
    left, right = 0, len(ls)-1
    while left <= right:  # 此处保留等号是为了验证边界值
        mid = (left+right)//2
        if ls[mid] == target:
            return mid
        elif ls[mid] < target:
            left = mid+1
        elif ls[mid] > target:
            right = mid-1
    return None
```

### 10.1  实现求解平方根的函数 69

```python
def mySqrt(self, x: int) -> int:
    if x == 0 or x == 1:
        return x
    left, right = 0, x
    while left <= right:
        mid = (left+right)//2
        if (mid == x//mid):
            return mid
        if (mid > x//mid):
            right = mid-1
        else:
            left = mid+1
            res = mid
    return res
```



## 11. 字典树

定义：Tried——字典树：查询效率比哈希表高
核心：用空间换时间

```python
class TrieNode:
    def __init__(self):
        self.children = [None] * ALPHABET_SIZE
        self.isEndOfWord = False
```

性质：
		根节点不包含字符
		从根到某一节点，将路径上经过的字符连接，为该节点对应的字符串
		每个节点的所有子节点包括的字符都不相同

### 11.1  实现字典树 208

```python
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.end_of_word = "#"

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for char in word:
            # 若char存在于node中，返回key对应的value；如果键不存在，将会添加键并将值设为{}。
            node = node.setdefault(char, {})
        node[self.end_of_word] = self.end_of_word

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for char in word:
            if char not in node:
                return False
            node = node[char]
        return self.end_of_word in node

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for char in prefix:
            if char not in node:
                return False
            node = node[char]
        return True
```



### 11.2  二维网格中的单词搜索问题212

```python
def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
    self.dx = [-1, 1, 0, 0]
    self.dy = [0, 0, -1, 1]
    self.END_OF_WORD = "#"
    if not board or not board[0] or not words:
        return []

    self.result = set()
    # 单词插入字典树
    root = collections.defaultdict()
    for word in words:
        node = root
        for char in word:
            node = node.setdefault(char, collections.defaultdict())
        node[self.END_OF_WORD] = self.END_OF_WORD

    self.m, self.n = len(board), len(board[0])
    for i in range(self.m):
        for j in range(self.n):
            if board[i][j] in root:
                self._dfs(board, i, j, "", root)
    return self.result

def _dfs(self, board, i, j, cur_word, cur_dict):
    cur_word += board[i][j]
    cur_dict = cur_dict[board[i][j]]

    if self.END_OF_WORD in cur_dict:
        self.result.add(cur_word)

    tmp, board[i][j] = board[i][j], '@'
    for k in range(4):  # 上下左右四个方向
        x, y = i + self.dx[k], j+self.dy[k]
        if 0 <= x < self.m and 0 <= y < self.n and board[x][y] != '@' and board[x][y] in cur_dict:
            self._dfs(board, x, y, cur_word, cur_dict)
    board[i][j] = tmp
```



## 12. 位运算

实战常用：
		x&1 == 1 or 0 ——判断奇数偶数（类似于x%2 == 1）
		x=x&(x-1) ——清零最低位的1
		x&-x——得到最低位的1

### 12.1  统计位1的个数 191

```python
def hammingWeight(self, n: int) -> int:
    # 方法一 位运算
    count = 0
    while n:
        n = n & (n-1)  # 清零最低位的1
        count += 1
    return count

    # 方法二 更快速
    count = 0
    while n:
        if n & 1: #判断二进制末尾是0还是1
            count += 1
        n >>= 1

    return count
```

### 12.2  2的幂次方 231

```python
def isPowerOfTwo(self, n: int) -> bool:
    return n != 0 and n & (n-1) == 0
    # 位运算，如果是2的幂方，则只有2进制下仅有一个1
```

### 12.3  比特位计数问题 338

```python
def countBits(self, num: int) -> List[int]:
    # 方法一 暴力法 O(N^2)
    def sumupBits(n):
        count = 0
        while n:
            if n & 1:
                count += 1
            n >>= 1
        return count
    ls = []
    for i in range(num+1):
        ls.append(sumupBits(i))
    return ls

    # 方法二 DP递推
    count = [0]*(num+1)

    for i in range(1, num+1):
        count[i] = count[i & (i-1)]+1
    return count
```



## 13. 动态规划

1. 递归+记忆化 ——> 递推	自下而上

2. 状态定义：`opt[n] dp[n] fib[n]`

3. 状态转移方程：`opt[n] = best_of(opt[n-1],opt[n-2],...)`

4. 得到最优子结构

   ```java
   int fib(int n, int[] memo){
       if (n<=0) return 0;
       else if (n==1) return 1;
       else if !(memo[n])
           memo[n] = fib(n-1)+fib(n-2);
       return memo[n]
   }
   ```

   DP —— 记录局部最优子结构

   贪心 —— 永远局部最优

   回溯（递归）——重复计算

### 13.1  爬楼梯 70

```python
# 方法一： 公式法
def climbStairs(self, n: int) -> int:
    x, y = 1, 1
    for _ in range(1, n):
        x, y = y, x+y
    return y

# 方法二：动态规划法
def climbStairs(self, n: int) -> int:
    if n <= 0:
        return False
    if n == 1:
        return 1
    self.memo = [0]*n
    self.memo[0] = 1
    self.memo[1] = 2

    def helper(n):
        if self.memo[n] == 0:
            self.memo[n] = helper(n-1)+helper(n-2)
        return self.memo[n]

    return helper(n-1)

```

### 13.2  三角形的最小路径和 120

```python
def minimumTotal(self, triangle: List[List[int]]) -> int:
    # 方法一 直接对动态规划来解释
    dp = [[0]*len(triangle)]*len(triangle[-1])
    for j in range(len(triangle[-1])):
        dp[len(triangle)-1][j] = triangle[len(triangle)-1][j]
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            dp[i][j] = min(dp[i+1][j], dp[i+1][j+1])+triangle[i][j]
    return dp[0][0]

    # 方法二
    res = triangle[-1]  # 把最后一行list浅复制给res
    for i in range(len(triangle)-2, -1, -1):
        for j in range(len(triangle[i])):
            res[j] = min(res[j], res[j+1]) + triangle[i][j]
    return res[0]
```

### 13.3  乘积最大子序列 152

```python
def maxProduct(self, nums: List[int]) -> int:
    if nums is None:
        return 0

    dp = [[0]*2 for _ in range(2)]
    # 0为正，1为负
    res, dp[0][0], dp[0][1] = nums[0], nums[0], nums[0]
    for i in range(1, len(nums)):
        x, y = i % 2, (i-1) % 2
        dp[x][0] = max(dp[y][0]*nums[i], dp[y][1]*nums[i], nums[i])
        dp[x][1] = min(dp[y][0]*nums[i], dp[y][1]*nums[i], nums[i])
        res = max(res, dp[x][0])
    return res
```

### 13.4  股票买卖系列



### 13.5  最长上升子序列 300

```python
def lengthOfLIS(self, nums: List[int]) -> int:
    if not nums:
        return 0
    dp = [1 for _ in range(len(nums))]
    res = 1
    for i in range(len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[j]+1, dp[i])
        res = max(dp[i], res)
    return res
```

### 13.6  零钱兑换 322

```python
def coinChange(self, coins: List[int], amount: int) -> int:
    if not coins or not amount:
        return 0
    dp = [amount+1 for _ in range(amount+1)]
    dp[0] = 0

    for i in range(1, 1+amount):
        for j in range(len(coins)):
            if coins[j] <= i:
                dp[i] = min(1+dp[i-coins[j]], dp[i])

    return -1 if dp[amount] > amount else dp[amount]
```

### 13.7  编辑距离 72

```python
def minDistance(self, word1: str, word2: str) -> int:
    word = [[0 for _ in range(len(word2)+1)] for _ in range(len(word1)+1)]
    for i in range(len(word1)+1):
        word[i][0] = i
    for i in range(len(word2)+1):
        word[0][i] = i

    for i in range(1, len(word1)+1):
        for j in range(1, len(word2)+1):
            word[i][j] = min(1+word[i-1][j], 1+word[i][j-1], word[i-1]
                                [j-1]+(0 if word1[i-1] == word2[j-1] else 1))
    return word[len(word1)][len(word2)]
```



## 14. 并查集

小弟找老大、帮派识别
并查集（Union & Find）

```python
class QuickUnionUF:
    def __init__(self):
        self.roots = []

    def QuickUnionUF(self, N):
        self.roots = [i for i in range(N)]

    def findRoot(self, i):
        root = i 
        # 找到真正的root————找到大boss
        while root != self.roots[root]:
            root = self.roots[root]
        # 路径压缩
        while i != self.roots[i]:
            self.roots[i], root = root, self.roots[i]
        return root

    def connect(self, p, q):
        return self.findRoot(p) == self.findRoot(q)

    def union(self, p, q):
        proot, qroot = self.findRoot(p), self.findRoot(q)
        self.roots[proot] = qroot
```



### 14.1  岛屿的个数 200

1. 染色 FloodFill		BFS / DFS
2. 并查集
   a. 初始化，正对“1”节点。
   b. 遍历所有节点，相邻合并 。      “1”合并，“0”不管
   c. 遍历 Parents

### 14.2  朋友圈547

## 15. LRU Cache

### 15.1  设计和实现一个LRU Cache缓存机制

## 16. 布隆过滤器