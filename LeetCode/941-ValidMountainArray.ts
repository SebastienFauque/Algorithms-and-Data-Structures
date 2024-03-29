// 941. Valid Mountain Array
// Easy

// 1286

// 114

// Add to List

// Share
// Given an array of integers arr, return true if and only if it is a valid mountain array.

// Recall that arr is a mountain array if and only if:

// arr.length >= 3
// There exists some i with 0 < i < arr.length - 1 such that:
// arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
// arr[i] > arr[i + 1] > ... > arr[arr.length - 1]



// Example 1:

// Input: arr = [2,1]
// Output: false
// Example 2:

// Input: arr = [3,5,5]
// Output: false
// Example 3:

// Input: arr = [0,3,2,1]
// Output: true


// Constraints:

// 1 <= arr.length <= 104
// 0 <= arr[i] <= 104
// Accepted
// 212,152
// Submissions
// 655,839


// Solved in O(n), specifically O(3n) because there are 3 loops:
// one on line 51, 58, and 62. Space complexity is O(1).
const validMountainArray = function(arr: number[]): boolean {
  if (!arr || arr.length <= 2) return false;

  const maxValue: number = Math.max(...arr);
  const maxIndex: number = arr.indexOf(maxValue);

  // Solve for cliff condition edge cases
  if (maxIndex === arr.length - 1) return false;
  if (maxIndex === 0) return false;

  for (let i = 0; i < maxIndex; i++) {
      if (arr[i] >= arr[i+1]) return false;
  }

  for (let i = maxIndex; i < arr.length; i++) {
      if (arr[i] <= arr[i+1]) return false;
  }

  return true;
};