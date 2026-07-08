class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for char in s:
            s_dict[char] = 1 + s_dict.get(char, 0)
        for char in t:
            t_dict[char] = 1 + t_dict.get(char, 0)
        s_list = s_dict.items()
        t_list = t_dict.items()
        for i in s_list:
            if i not in t_list:
                return False
        for i in t_list:
            if i not in s_list:
                return False
        return True