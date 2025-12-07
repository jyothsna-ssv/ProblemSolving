# sort products- insert into tries
# each node stores upto 3 
# for each prefix of searchWord, walk the Trie and return the stored list
# if a prefix fails, all the remaining suggestions are empty

class TrieNode:
    def __init__(self):
        self.children={}
        self.words=[]
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()

        root=TrieNode()
        for word in products:
            node=root
            for ch in word:
                if ch not in node.children:
                    node.children[ch]=TrieNode()
                node=node.children[ch]
                if len(node.words)<3:
                    node.words.append(word)
        res=[]
        node=root
        for ch in searchWord:
            if ch in node.children:
                node=node.children[ch]
                res.append(node.words)
            else:
                while len(res)<len(searchWord):
                    res.append([])
                break
        return res