/**
 * LeetCode problem: 11
 * Difficulty: Medium
 * Solved in O(n) time complexity with O(1) space complexity
 *
 *Given n non-negative integers a1, a2, ..., an , where each represents a
 *point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints
 *of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the x-axis
 *forms a container, such that the container contains the most water.
 *Notice that you may not slant the container.
 *
 */

const maxArea = function(height) {
  let l = 0,
      r = height.length - 1,
      res = 0;

  while (l < r) {
      const high = Math.min(height[l], height[r]);
      const width = r - l;
      res = Math.max(res, (high * width));

      if (height[l] > height[r]) r--;
      else l++;
  }
  return res;
};