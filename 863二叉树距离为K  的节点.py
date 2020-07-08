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
        self.path_root2target = [] # 从root到target的沿线节点
        self.all_path_root2target = []
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        target = self.searchTarget(root,target)
        if target == None:
            return []
        self.searchKsteps_down(target,K) # 往下找








    # 从root出发往下搜索k步
    def searchKsteps_down(self, root, K):
        if K == 0:
            self.k_steps_nodes.append(root.val)
            return root
        if root is None:
            return root
        if root.left:
            self.searchKsteps_down(root.left, K - 1)
        if root.right:
            self.searchKsteps_down(root.right, K - 1)

    # 往上搜索
    # def searchKsteps_up(self,target,K):
    #     for path in self.all_path_root2target:
    #         if len(path)>=3:
    #             self.k_steps_nodes.append(path[-2].val)  # 倒数第三个
    #         else:
    #             self.searchKsteps_down(target.right,K-len(path))
    #             self.searchKsteps_down(target.left, K - len(path))




    # 搜索目标
    # def searchTarget(self,root,target,steps):
    #     if root is None:
    #         return root
    #     if root.val == target:
    #         self.path_root2target.append(root)
    #         self.all_path_root2target(self.path_root2target)
    #         return root
    #     self.path_root2target.append(root)
    #     if root.left:
    #         self.searchTarget(root.left,target,steps+1)
    #     if root.right:
    #         self.searchTarget(root.right,target,steps+1)



