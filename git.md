```python
    #告诉计算机我是谁
    git config --global user.name 'xyf'
    git config --global user.email ''
      
    #初始化
    git init
      
    #递交到暂存区
    git add demo.py
    git add . #所有文件提交
      
    #递交到版本库
    git commit -m '描述'
      
    #历史日志
    git log
      
    #撤销上一次提交，并将暂存区的文件重新提交
    git commit --amend
      
    #撤回到上一版本 暂存区拉到工作区
    git checkout -- python代码笔记.md
    git checkout -- .   #所有文件修改
      
    #拉去最近一次提交到版本库的文件到暂存区，该操作不影响工作区
    git reset HEAD python代码笔记.md
    
    #分支
    git branch
    git branch dev #新建分支
    #切换分支
    git checkout dev
    #删除分支
    git branch -d dev
    
    #比较差异
    git diff
    
    #把本地代码push到repository
    git push https://github.com/David-xyf/python-code.git
    
    
```

