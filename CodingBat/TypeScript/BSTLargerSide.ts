/**
 * Suppose you're given a binary tree represented as an array.
 * For example, [3, 6, 2, 9, -1, 10] represents the following
 * binary tree (where -1 is a non-existent node):
 *
 *        3
 *      /    \
 *     6      2
 *    /      /
 *   9      10
 *
 * Write a function that determines whether the left or right
 *  branch of the tree is larger. The size of each branch is
 * the sum of the node values. The function should return
 * the string "Right" if the right side is larger and "Left" if
 * the left side is larger. If the tree has 0 nodes or if the
 * size of the branches are equal, return the empty string.
 *
 * Example input: [3, 6, 2, 9, -1, 10]
 * Example Output: Left
 *
 */




const solution = (arr: number[]) => {
  // Type your solution here
  if (!arr || !arr.length || arr.length === 1) return '';

  let halfRowLength: number = 1;
  let left: number = 0;
  const leftArr: number[] = [];
  let right: number = 0;
  const rightArr: number[] = [];

  // split array into levels
  for (let i: number = 1; i < arr.length; i++) {
      if (left < halfRowLength && arr[i] !== -1 && arr[i] !== 0) {
          leftArr.push(arr[i]);
          left++;
      } else if (arr[i] !== -1 && arr[i] !== 0) {
          rightArr.push(arr[i]);
          right++;
      }

      if (right === halfRowLength) {
          halfRowLength *= 2;
      }
  }

  left = leftArr.reduce((a, b) => { return a + b }, 0);
  right = rightArr.reduce((a, b) => { return a + b }, 0);

  if (left === right) return '';
  else { return left > right ? "Left" : "Right"};
};



console.log(solution([3, 6, 2, 9, -1, 10])); // Left
console.log(solution([1, 4, 100, 5])); // Right
console.log(solution([1, 10, 5, 1, 0, 6])); // ''
console.log(solution([])); // ''
console.log(solution([1])); // ''