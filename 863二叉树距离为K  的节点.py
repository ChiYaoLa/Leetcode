# -*- coding: utf-8 -*-
# @Time    : 2020/7/8 23:02
"""
https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree/solution/jian-ji-qing-xi-yi-dong-san-ge-bu-zou-dfs-xiang-xi/

"""
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 解法一 递归+节点距离
class Solution(object):
    def __init__(self):
        self.k_steps_nodes = [] # 距离为K的节点值
        self.targetNode = None

    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.dfs(root,target)
        if self.targetNode == None:
            return []
        self.searchKsteps(target,K) # 往下找
        i = K
        while(self.targetNode.parent and i != 0):  # 向上找
            self.targetNode = self.targetNode.parent
            self.searchKsteps(self.targetNode,i-1)

        return self.k_steps_nodes


    # 寻找target
    def dfs(self,root,target):
        if root is None:
            return root
        if root.val == target.val:
            self.targetNode = root
        if root.left:
            root.left.parent = root # 顺手改指针指向
            self.dfs(root.left,target)
        if root.right:
            root.right.parent = root
            self.dfs(root.right,target)


    # 从root出发往下搜索k步
    def searchKsteps(self, root, K):
        if K == 0:
            self.k_steps_nodes.append(root.val)
            return root
        if root is None:
            return root
        if root.left:
            self.searchKsteps(root.left, K-1)
        if root.right:
            self.searchKsteps(root.right, K -1)





