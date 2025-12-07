# nested disct
# insert-> create nodes, mark end with #
# search-> follow path, valid only if end marker exists
# startsWith -> follow path, no need for end marker


class Trie:

    def __init__(self):
        self.root={}
        self.END="#"
        

    def insert(self, word: str) -> None:
        node=self.root
        for ch in word:
            if ch not in node:
                node[ch]={}
            node=node[ch]
        node[self.END]=True


    def search(self, word: str) -> bool:
        node=self.root
        for ch in word:
            if ch not in node:
                return False
            node=node[ch]
        return self.END in node


    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node:
                return False
            node=node[ch]
        return True

        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)