# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 10:52
"""
https://leetcode-cn.com/problems/add-and-search-word-data-structure-design/
"""
class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.look_up = {}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree = self.look_up
        for a in word:
            if a not in tree:
                tree[a] = tree
            


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)