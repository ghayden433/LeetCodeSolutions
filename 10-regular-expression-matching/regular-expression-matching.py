class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        #cache for memoization
        cache = {}

        def dfs(i, j):
            #if we've already checked (i, j) return immediately to save computation
            if (i, j) in cache:
                return cache[(i, j)]

            #base cases
            #if i and j are out of bounds the string matches
            if i >= len(s) and j >= len(p): 
                return True
            #if just j is out of bounds it does not match as there is still string left and no pattern
            if j >= len(p): 
                return False

            #bool to see if the character matches the pattern
            match = i < len(s) and (s[i] == p[j] or p[j] == ".")

            #if the next char in p is a star
            if (j + 1) < len(p) and p[j + 1] == "*":
                # do the next char in s using the star or no star, and store in cache
                cache[(i, j)] = (dfs(i, j + 2) or (match and dfs(i + 1, j)))
                return cache[(i, j)]
            # if there is no star but the char matches
            if match:
                # move to the next char in s and bit of pattern in p
                cache[(i, j)] = dfs(i + 1, j + 1)
                return cache[(i, j)]
            #otherwise return false because it does not match
            cache[(i, j)] = False
            return False

        return dfs(0,0)