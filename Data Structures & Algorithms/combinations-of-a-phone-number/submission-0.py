class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        lookup = {
            '2': ("a", "b", "c"),
            '3': ("d", "e", "f"),
            '4': ("g", "h", "i"),
            '5': ("j", "k", "l"),
            '6': ("m", "n", "o"),
            '7': ("p", "q", "r", "s"),
            '8': ("t", "u", "v"),
            '9': ("w", "x", "y", "z"),
        }

        out = []

        def backtrack(index,path):
            if len(path) == len(digits):
                out.append(path[:])
                return
            for let in lookup[digits[index]]:
                path+=let
                backtrack(index+1,path)
                path = path[:-1]
        
        backtrack(0,"")
        return out


