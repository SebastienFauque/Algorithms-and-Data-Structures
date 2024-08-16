class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # trim whitespace from left and right side of string
        s = s.strip()
        # split strings into a list based on whitespace
        # remove all strings in list that have no alpha characters
        l = s.split()
        
        # return length of last string in the remaining list
        return len(l[-1])
