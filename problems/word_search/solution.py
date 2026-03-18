class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        """Implement your Word Search solution here."""
            #path: [(i, j)]
        #helper function
        def path_to_word(path):
            letter_arr = []
            for i, j in path:
                letter_arr.append(board[i][j])
            return "".join(letter_arr)
            
        res = False
        #options: [(i, j)]
        def backtrack(options, path):
            nonlocal res
            word_so_far = path_to_word(path)
            if word_so_far == word:
                res = True
                return
            if word_so_far != word[:len(word_so_far)]:
                return
            for i, j in options:
                if (i, j) in path:
                    continue
                if (i < 0 or i >= len(board)) or (j < 0 or j >= len(board[0])):
                    continue
                path.append((i, j))
                new_options = [(i-1, j), (i, j+1), (i, j-1), (i+1, j)]
                backtrack(new_options, path)
                path.pop()
        
        initial_options = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                initial_options.append((i, j))
        backtrack(initial_options, [])
        return res
