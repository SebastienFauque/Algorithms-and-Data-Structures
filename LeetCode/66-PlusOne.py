class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] != 9:
            digits[-1] = digits[-1] + 1
            return digits
        
        else:
            # Recursion solution
            # if idx [-2] exists, recurse without last element, on return add the last element.
            try:
                digits[-2]
                return self.plusOne(digits[:-1]) + [0]
            # else add the [-2] element as a 0 and recurse on return add the last element.
            except IndexError:
                return self.plusOne([0] + digits[:-1]) + [0]
