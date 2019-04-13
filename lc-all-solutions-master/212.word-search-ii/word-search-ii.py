#https://www.youtube.com/watch?v=x02b8zfvGFU

class TrieNode:
    def __init__(self, char):
        self.neighbours = {}
        self.isWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode("-")
        
    def addWord(self, word):
        root = self.root
        for i in xrange(0, len(word)):
            c = word[i]
            if c in root.neighbours:
                root = root.neighbours[c]
            else:
                newnode = TrieNode(c)
                root.neighbours[c] = newnode
                root = root.neighbours[c]
        root.isWord = True


class Solution:
    # @param board, a list of lists of 1 length string
    # @param words: A list of string
    # @return: A list of string
    def findWords(self, board, words):
        # write your code here
        trie = Trie()
        res = []
        visited = [[0] * len(board[0]) for i in xrange(0, len(board))]
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        def dfs(i, j, board, visited, res, root, path):
            if not root:
                return
            
            if root.isWord:
                res.append(path)
                
            for direction in directions:
                ni, nj = i + direction[0], j + direction[1]
                if 0 <= ni < len(board) and 0 <= nj < len(board[0]):
                    c = board[ni][nj]
                    if visited[ni][nj] == 0:
                        visited[ni][nj] = 1
                        dfs(ni, nj, board, visited, res, root.neighbours.get(c, None), path + c)
                        visited[ni][nj] = 0

        for word in words:
            trie.addWord(word)
        root = trie.root
        for i in range(0, len(board)):
            for j in range(0, len(board[0])):
                c = board[i][j]
                visited[i][j] = 1
                dfs(i, j, board, visited, res, root.neighbours.get(c, None), c)
                visited[i][j] = 0
        return list(set(res))




# Time:  O(m * n * l)
# Space: O(l)
#
# Given a 2D board and a list of words from the dictionary, find all words in the board.
#
# Each word must be constructed from letters of sequentially adjacent cell, where "adjacent" cells 
# are those horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.
#
# For example,
# Given words = ["oath","pea","eat","rain"] and board =
#
# [
#   ['o','a','a','n'],
#   ['e','t','a','e'],
#   ['i','h','k','r'],
#   ['i','f','l','v']
# ]
# Return ["eat","oath"].
# Note:
# You may assume that all inputs are consist of lowercase letters a-z.
#

class TrieNode(object):
    # Initialize your data structure here.
    def __init__(self):
        self.is_string = False
        self.leaves = {}

    # Inserts a word into the trie.
    def insert(self, word):
        cur = self
        for c in word:
            if not c in cur.leaves:
                cur.leaves[c] = TrieNode()
            cur = cur.leaves[c]
        cur.is_string = True


class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        visited = [[False for j in xrange(len(board[0]))] for i in xrange(len(board))]
        result = {}
        trie = TrieNode()
        for word in words:
            trie.insert(word)
            
        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if self.findWordsRecu(board, trie, 0, i, j, visited, [], result):
                    return True
        
        return result.keys()
    
    def findWordsRecu(self, board, trie, cur, i, j, visited, cur_word, result):
        if not trie or i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or visited[i][j]:
            return
        
        if board[i][j] not in trie.leaves:
            return
        
        cur_word.append(board[i][j])
        next_node = trie.leaves[board[i][j]]
        if next_node.is_string:
            result["".join(cur_word)] = True
        
        visited[i][j] = True
        self.findWordsRecu(board, next_node, cur + 1, i + 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, cur + 1, i - 1, j, visited, cur_word, result)
        self.findWordsRecu(board, next_node, cur + 1, i, j + 1, visited, cur_word, result)
        self.findWordsRecu(board, next_node, cur + 1, i, j - 1, visited, cur_word, result)     
        visited[i][j] = False
        cur_word.pop()