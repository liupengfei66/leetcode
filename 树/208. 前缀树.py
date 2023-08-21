# Trie（发音类似 "try"）或者说 前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。
# https://leetcode.cn/problems/implement-trie-prefix-tree/description/
# 时间复杂度 insert O(n) n-字符串长度，空间复杂度O(n) 最坏可能n个字符都不相同
# search 时间O(n)


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert a word into the Trie
    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    # Search for a word in the Trie
    def search(self, word):
        node = self.root   # 保证我们始终可以访问到树的根节点
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    # Check if there's any word in the Trie that starts with the given prefix
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True
    
    def print(self, space_between="  "):  # Use two spaces between values by default
        if not self.root.children:
            print("Trie is empty!")
            return

        queue = [(self.root, None, 0)]  # Second value is parent's value, third value is level
        current_level = 0
        while queue:
            node, parent_value, level = queue.pop(0)
            
            # Check if we are entering a new level
            if level != current_level:
                current_level = level
                print()  # Print newline for new level

            for char, child in node.children.items():
                # Print in the format "parent:child"
                print(f"{parent_value if parent_value else 'ROOT'}:{char}" + space_between, end="")
                queue.append((child, char, level + 1))

# Test the Trie with the given set of words
trie = Trie()
words = ["app", "apple", "bat", "batman", "batmobile", "batik", "baton"]

for word in words:
    trie.insert(word)

# Checking if the words "app", "batik" and "car" are present in the Trie
test_words = ["app", "batik", "car"]
results = {word: trie.search(word) for word in test_words}

print(results)
trie.print()
