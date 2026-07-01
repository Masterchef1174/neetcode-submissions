class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Check if length of strings not equal
        if len(s) != len(t):
            return False
    
        s_count = {}
        for s_char in s:
            if s_char not in s_count:
                s_count[s_char] = 1
            else:
                s_count[s_char] += 1

        t_count = {}
        for t_char in t:
            if t_char not in t_count:
                t_count[t_char] = 1
            else:
                t_count[t_char] += 1

        # for k,v in s_count.items():
        #     if t_count.get(k, None) == None or t_count.get(k, None) != v:
        #         return False

        return s_count == t_count