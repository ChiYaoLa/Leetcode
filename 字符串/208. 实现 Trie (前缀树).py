# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 10:22

"""
https://leetcode-cn.com/problems/implement-trie-prefix-tree/
"""

class Trie:
    """
    abc ab
    {"a":
    {"b":
    {"#":"#","c":{"#":"#"}}  }

    }

    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.look_up = {}


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        tree = self.look_up
        for a in word:
            if a not in tree:
                tree[a] = {}
            tree = tree[a]
        tree["#"] = "#"


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        tree = self.look_up
        for a in word:
            if a not in tree: # 先排除不行的，在处理行的
                return False
            tree = tree[a]
        if "#" in tree:
            return True
        return False


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        tree = self.look_up
        for a in prefix:
            if a not in tree:
                return False
            tree = tree[a]
        return True



# Your Trie object will be instantiated and called as such:
# word = "abc"
# # obj = Trie()
# # obj.insert(word)
# # param_2 = obj.search(word)
# # param_3 = obj.startsWith("abc")

