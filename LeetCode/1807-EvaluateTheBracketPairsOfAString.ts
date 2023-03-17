/**
 * LeetCode problem: 1807. Evaluate the Bracket Pairs of a String
 * Difficulty: Medium
 * Solved in O(2n) time complexity with O(n) space complexity
 *
 *
 * You are given a string s that contains some bracket pairs, with each pair containing a non-empty key.
 * For example, in the string "(name)is(age)yearsold", there are two bracket pairs that contain the keys "name" and "age".
 * You know the values of a wide range of keys. This is represented by a 2D string array knowledge where each knowledge[i] = [keyi, valuei] indicates that key keyi has a value of valuei.
 *
 *You are tasked to evaluate all of the bracket pairs. When you evaluate a bracket pair that contains some key keyi, you will:
 *
 *Replace keyi and the bracket pair with the key's corresponding valuei.
 *If you do not know the value of the key, you will replace keyi and the bracket pair with a question mark "?" (without the quotation marks).
 *Each key will appear at most once in your knowledge. There will not be any nested brackets in s.
 *
 *Return the resulting string after evaluating all of the bracket pairs.
Example 1:

Input: s = "(name)is(age)yearsold", knowledge = [["name","bob"],["age","two"]]
Output: "bobistwoyearsold"
Explanation:
The key "name" has a value of "bob", so replace "(name)" with "bob".
The key "age" has a value of "two", so replace "(age)" with "two".
 */

var evaluate = function(s, knowledge): string {
  let sCopy: string = JSON.parse(JSON.stringify(s));

  const regex = /(\([a-z]*\))/gm
  let sArr: string[] = sCopy.split(regex);

  const know: object = {};
  for (let i = 0; i < knowledge.length; i++) {
    know[knowledge[i][0]] = knowledge[i][1];
  }

  sArr.forEach((val, index) => {
    if (regex.test(val)) {
        let sub: string = val.substring(1, val.length - 1)
        if (know.hasOwnProperty(sub)) sArr[index] = know[sub];
        else sArr[index] = '?';
      }
  })

  return sArr.join('');
};


console.log(evaluate("(name)is(age)yearsold", [["name","bob"],["age","two"]]));