
class WordDictionary:
    def __init__(self):
        self.root = {}

    def addWord(self, word: str) -> None:
        curr_node = self.root
        for char in word:
            curr_node.setdefault(char, {})
            curr_node = curr_node[char]
        curr_node["*"] = {}

    def search(self, word: str) -> bool:
        # similar to BFS
        search_nodes = [self.root]
        for char in word:
            new_nodes = []
            for curr_search_node in search_nodes:
                # print(f"{curr_search_node = }")
                if char == ".":
                    new_nodes += [val for val in curr_search_node.values()]
                elif char in curr_search_node:
                    new_nodes.append(curr_search_node[char])
                # print(char, new_nodes)

            search_nodes = new_nodes

        return any("*" in node for node in search_nodes)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

