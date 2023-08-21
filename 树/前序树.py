# List = [cartefdxh, cart, carlkijfwe, chdfwef, cafkekfld]
# 现在给定一个字符串“cart”，输出该字符串在List中作为前缀出现的次数。

class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.count += 1

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return 0
            node = node.children[char]
        return node.count

def count_occurrences_with_trie(string, large_list):
    trie = Trie()
    for item in large_list:
        trie.insert(item)
    return trie.search(string)

# 示例用法
large_list = [ 'cartefdxh', 'cart', 'carlkijfwe', 'chdfwef', 'cafkekfld']  # 假设这是一个非常大的list，包含各种元素
target_string = "cart"  # 要查找的字符串
occurrences = count_occurrences_with_trie(target_string, large_list)
print("字符串 '{}' 在list中出现的次数：{}".format(target_string, occurrences))
