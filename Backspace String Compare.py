class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def get_next_valid_char_index(s, index):
            skip_backspaces = 0
            while index >= 0:
                if s[index] == '#':
                    skip_backspaces += 1
                elif skip_backspaces > 0:
                    skip_backspaces -= 1
                else:
                    break
                index -= 1
            return index

        s_ptr = len(s) - 1
        t_ptr = len(t) - 1

        while s_ptr >= 0 or t_ptr >= 0:
            s_ptr = get_next_valid_char_index(s, s_ptr)
            t_ptr = get_next_valid_char_index(t, t_ptr)

            if s_ptr < 0 and t_ptr < 0:
                return True
            if s_ptr < 0 or t_ptr < 0 or s[s_ptr] != t[t_ptr]:
                return False

            s_ptr -= 1
            t_ptr -= 1

        return True
