# 704. Binary Search
# Recursive Binary Search
# time complexity: O(log n)
# space complexity: O(log n) due to recursion stack, can be O(1) with iterative approach

class Solution: 
    def bin_search(self, nums: List[int], target: int, l=0, r=0) -> int:
        centerIdx = (r + l) // 2

        if l > r:
            return -1
        elif nums[centerIdx] == target:
            return centerIdx
        elif nums[centerIdx] > target:
            return self.bin_search(nums, target, l, centerIdx - 1)
        elif nums[centerIdx] < target:
            return self.bin_search(nums, target, centerIdx + 1, r)

    def search(self, nums: List[int], target: int, l=0, r=0) -> int:
        return self.bin_search(nums, target, 0, len(nums) - 1):