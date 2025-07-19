from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0
        
        if len(nums) == 1:
            return 1
        
        nums = sorted(nums)
        max = 0
        count = 1

        i=0
        while i < len(nums) - 1:
            if count > max:
                max = count

            current = nums[i]
            nxt = nums[i+1]
            if current + 1 == nxt:
                count += 1
            elif current == nxt:
                count += 1
            else:
                if count > max:
                    max = count
                count = 0
            i += 1

        if count > max:
            max = count



        return max


testData = [0,3,2,5,4,6,1,1]

if __name__ == "__main__":
    s = Solution()
    # print('####', s.longestConsecutive(testData))  # Output: 7
    print(s.longestConsecutive([0, -1]))        # Output: 2
    # print(s.longestConsecutive([1]))       # Output: 1
    # print(s.longestConsecutive([1,2,3,4,5]))  # Output: 5
    # print(s.longestConsecutive([100,4,200,1,3,2]))  # Output: 4