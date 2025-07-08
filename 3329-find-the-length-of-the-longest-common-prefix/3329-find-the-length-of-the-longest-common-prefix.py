class TrieNode:
    def __init__(self):
        self.children = {}

class Solution(object):
    def longestCommonPrefix(self, arr1, arr2):
        
        root = TrieNode()
        for n in arr2:
            node = root
            for digit in str(n):
                if digit not in node.children:
                    node.children[digit] = TrieNode()
                node = node.children[digit]
        
        max_len = 0
        for n in arr1:
            node = root
            prefix_len = 0
            for digit in str(n):
                if digit in node.children:
                    prefix_len +=1
                    node = node.children[digit]
                else:
                    break
            max_len = max(max_len,prefix_len)
        return max_len
        